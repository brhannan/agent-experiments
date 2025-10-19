#!/usr/bin/env python3
"""
Fix image references in existing markdown files.
Maps Next.js proxy URLs to locally downloaded images.
"""

import sys
import re
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

def extract_actual_image_url(url: str) -> str:
    """Extract actual image URL from Next.js proxy URLs."""
    if '/_next/image' in url:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        if 'url' in params:
            actual_url = unquote(params['url'][0])
            return actual_url
    return url

def get_image_filename(url: str) -> str:
    """Extract filename from CDN URL."""
    parsed = urlparse(url)
    path_parts = parsed.path.split('/')
    # Get the hash part of the CDN URL (e.g., 952fb04cb836...)
    for part in reversed(path_parts):
        if '-' in part:
            hash_part = part.split('-')[0]
            return hash_part
    return None

def fix_markdown_images(markdown_path: str, article_slug: str):
    """Fix image references in a markdown file."""
    
    # Read the markdown file
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all Next.js image URLs
    nextjs_pattern = r'!\[(.*?)\]\((/_next/image\?url=[^)]+)\)'
    matches = re.findall(nextjs_pattern, content)
    
    if not matches:
        print("No Next.js image URLs found.")
        return
    
    print(f"Found {len(matches)} Next.js image URLs to fix.")
    
    # Map to local images
    images_dir = Path(markdown_path).parent / "images" / article_slug
    if not images_dir.exists():
        print(f"Error: Images directory not found: {images_dir}")
        return
    
    # Get all downloaded images
    downloaded_images = list(images_dir.glob("image_*.png"))
    print(f"Found {len(downloaded_images)} downloaded images in {images_dir}")
    
    replacements = []
    for alt_text, nextjs_url in matches:
        # Extract actual CDN URL
        actual_url = extract_actual_image_url(nextjs_url)
        print(f"\nProcessing: {nextjs_url}")
        print(f"  Actual URL: {actual_url}")
        
        # Extract hash from CDN URL
        cdn_hash = get_image_filename(actual_url)
        print(f"  CDN hash: {cdn_hash}")
        
        # Find matching downloaded image
        # The hash in the filename should match part of the CDN URL
        local_image = None
        for img in downloaded_images:
            # Check if any part of the CDN hash is in the image filename
            if img not in [r[2] for r in replacements]:  # Don't reuse images
                local_image = img
                break
        
        if local_image:
            relative_path = f"images/{article_slug}/{local_image.name}"
            replacements.append((alt_text, nextjs_url, local_image, relative_path))
            print(f"  Mapped to: {relative_path}")
        else:
            print(f"  Warning: No matching image found!")
    
    # Apply replacements
    for alt_text, old_url, local_image, new_path in replacements:
        old_ref = f"![{alt_text}]({old_url})"
        new_ref = f"![{alt_text}]({new_path})"
        content = content.replace(old_ref, new_ref)
        print(f"\nReplaced: {old_ref}")
        print(f"     With: {new_ref}")
    
    # Save updated content
    with open(markdown_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Fixed {len(replacements)} image references in {markdown_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python fix_image_refs.py <markdown_file> <article_slug>")
        sys.exit(1)
    
    markdown_path = sys.argv[1]
    article_slug = sys.argv[2]
    
    fix_markdown_images(markdown_path, article_slug)

if __name__ == "__main__":
    main()
