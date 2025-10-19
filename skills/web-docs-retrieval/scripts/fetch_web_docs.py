#!/usr/bin/env python3
"""
Web Documentation Retrieval Script

Fetches web content and saves it locally with images downloaded.
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Tuple, List, Optional
from urllib.parse import urljoin, urlparse, parse_qs, unquote
import hashlib

try:
    import requests
    from bs4 import BeautifulSoup
    import html2text
except ImportError:
    print("Error: Required packages not installed.")
    print("Please run: pip install requests beautifulsoup4 html2text")
    sys.exit(1)


class WebDocsRetriever:
    """Handles fetching and saving web documentation with images."""
    
    def __init__(self, base_dir: str = "/Users/bhannan/code/hello-world-agent"):
        self.base_dir = Path(base_dir)
        self.blogs_dir = self.base_dir / "blogs"
        self.images_dir = self.blogs_dir / "images"
        
        # Configure html2text for better markdown conversion
        self.html_converter = html2text.HTML2Text()
        self.html_converter.body_width = 0  # Don't wrap lines
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.single_line_break = False
        
    def slugify(self, text: str) -> str:
        """Convert text to kebab-case slug."""
        # Remove special characters and convert to lowercase
        text = re.sub(r'[^\w\s-]', '', text.lower())
        # Replace whitespace with hyphens
        text = re.sub(r'[-\s]+', '-', text)
        return text.strip('-')
    
    def fetch_content(self, url: str) -> Tuple[str, str, BeautifulSoup]:
        """Fetch web page content and return HTML, title, and BeautifulSoup object."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract title
            title = soup.find('title')
            title_text = title.get_text().strip() if title else "Untitled"
            
            # Try to find article title if available
            article_title = (
                soup.find('h1') or 
                soup.find('article') or 
                soup.find('meta', property='og:title')
            )
            if article_title:
                if hasattr(article_title, 'get_text'):
                    title_text = article_title.get_text().strip()
                elif article_title.get('content'):
                    title_text = article_title.get('content').strip()
            
            return response.text, title_text, soup
            
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch URL: {e}")
    
    def download_image(self, img_url: str, article_slug: str) -> Optional[str]:
        """Download an image and return the local path."""
        try:
            # Create article-specific image directory
            img_dir = self.images_dir / article_slug
            img_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate filename from URL
            parsed = urlparse(img_url)
            original_name = os.path.basename(parsed.path)
            
            # If no extension, try to detect from content-type
            if not original_name or '.' not in original_name:
                # Use hash of URL as filename
                url_hash = hashlib.md5(img_url.encode()).hexdigest()[:8]
                original_name = f"image_{url_hash}.png"
            
            local_path = img_dir / original_name
            
            # Download image
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            response = requests.get(img_url, headers=headers, timeout=30, stream=True)
            response.raise_for_status()
            
            # Save image
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Return relative path from blogs directory
            return f"images/{article_slug}/{original_name}"
            
        except Exception as e:
            print(f"Warning: Failed to download image {img_url}: {e}")
            return None
    
    def extract_actual_image_url(self, url: str) -> str:
        """Extract actual image URL from Next.js or other proxy URLs."""
        # Handle Next.js image optimization URLs like:
        # /_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2F...&w=3840&q=75
        if '/_next/image' in url:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            if 'url' in params:
                # Decode the URL-encoded actual image URL
                actual_url = unquote(params['url'][0])
                return actual_url
        
        return url
    
    def process_images(self, soup: BeautifulSoup, base_url: str, article_slug: str) -> dict:
        """Find all images and download them, return mapping of old to new URLs."""
        image_map = {}
        
        # Find all img tags
        for img in soup.find_all('img'):
            src = img.get('src')
            if not src:
                continue
            
            # Convert relative URLs to absolute
            if not src.startswith(('http://', 'https://')):
                src = urljoin(base_url, src)
            
            # Extract actual image URL (handles Next.js proxy URLs)
            actual_url = self.extract_actual_image_url(src)
            
            # Download image from actual URL
            local_path = self.download_image(actual_url, article_slug)
            if local_path:
                # Map BOTH the proxy URL and actual URL to the local path
                image_map[src] = local_path
                if actual_url != src:
                    image_map[actual_url] = local_path
        
        return image_map
    
    def convert_to_markdown(self, html: str, image_map: dict) -> str:
        """Convert HTML to markdown and update image references."""
        # Convert HTML to markdown
        markdown = self.html_converter.handle(html)
        
        # Update image references
        # Sort by length (longest first) to avoid partial replacements
        sorted_urls = sorted(image_map.keys(), key=len, reverse=True)
        
        for old_url in sorted_urls:
            new_path = image_map[old_url]
            # Handle both markdown ![alt](url) and HTML <img src="url"> formats
            markdown = markdown.replace(old_url, new_path)
        
        return markdown
    
    def generate_frontmatter(self, title: str, url: str, content: str) -> str:
        """Generate YAML frontmatter for the markdown file."""
        # Extract potential tags from content (simplified - could be enhanced with NLP)
        # For now, just provide empty array that can be manually filled
        tags = "[]"
        
        # Generate a brief description (first paragraph or first 200 chars)
        description_match = re.search(r'\n\n(.+?)(?:\n\n|\Z)', content, re.DOTALL)
        if description_match:
            description = description_match.group(1).strip()
            # Clean up markdown syntax
            description = re.sub(r'[#*`\[\]()]', '', description)
            # Truncate to reasonable length
            if len(description) > 200:
                description = description[:197] + "..."
        else:
            description = "Documentation retrieved from web."
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        frontmatter = f"""---
title: {title}
url: {url}
retrieved: {today}
tags: {tags}
description: {description}
---

"""
        return frontmatter
    
    def save_markdown(self, content: str, filename: str):
        """Save markdown content to file."""
        filepath = self.blogs_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Saved: {filepath}")
    
    def retrieve(self, url: str) -> str:
        """Main method to retrieve web documentation with images."""
        print(f"Fetching content from: {url}")
        
        # Fetch content
        html, title, soup = self.fetch_content(url)
        print(f"📄 Title: {title}")
        
        # Generate article slug
        article_slug = self.slugify(title)
        print(f"📝 Slug: {article_slug}")
        
        # Process images
        print("🖼️  Downloading images...")
        image_map = self.process_images(soup, url, article_slug)
        print(f"✅ Downloaded {len(image_map)} images")
        
        # Convert to markdown
        print("📝 Converting to markdown...")
        markdown = self.convert_to_markdown(html, image_map)
        
        # Generate frontmatter
        frontmatter = self.generate_frontmatter(title, url, markdown)
        
        # Combine frontmatter and content
        final_content = frontmatter + markdown
        
        # Save file
        filename = f"{article_slug}.md"
        self.save_markdown(final_content, filename)
        
        return filename


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python fetch_web_docs.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    try:
        retriever = WebDocsRetriever()
        filename = retriever.retrieve(url)
        print(f"\n✅ Successfully retrieved and saved to: blogs/{filename}")
        print(f"📁 Images saved to: blogs/images/{retriever.slugify(filename[:-3])}/")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
