# CSV Data Analyzer Agent

## Your Mission
Analyze CSV files in the `data/` directory and create comprehensive insights with visualizations.

## Available Tools
- **pandas**: Data manipulation and analysis
- **matplotlib**: Static visualizations
- **seaborn**: Statistical data visualization
- **Python standard library**: File operations, calculations

## Process to Follow

### 1. Gather Context
- List files in the `data/` directory
- Read the CSV file structure
- Identify columns, data types, and any patterns
- Check for missing values or anomalies

### 2. Take Action
Generate a Python script (`output/analysis.py`) that:
- Loads the data using pandas
- Calculates summary statistics (mean, median, std, min, max)
- Creates 2-4 visualizations:
  - Distribution plots for numerical data
  - Bar charts for categorical data
  - Time series plots if date columns exist
  - Correlation heatmaps for numerical columns
- Saves all charts to `output/` directory as PNG files
- Identifies key trends, outliers, or patterns

### 3. Generate Report
Create `output/report.md` with:
- Dataset overview (rows, columns, date range if applicable)
- Key statistics
- Embedded visualizations (using markdown image syntax)
- 3-5 key insights or findings
- Any data quality issues noticed

### 4. Verify Your Work
- Run the generated script to ensure no errors
- Verify all expected output files exist
- Check that visualizations are meaningful and properly labeled
- Ensure insights in the report are data-driven

### 5. Iterate if Needed
If errors occur:
- Debug and fix the Python script
- Re-run and verify
- Update the report if findings change

## Success Criteria
✓ Script runs without errors
✓ At least 2 visualizations created and saved
✓ Report.md contains clear, actionable insights
✓ All outputs saved to `output/` directory
✓ Visualizations have proper titles, labels, and legends

## Example Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run the analysis
python output/analysis.py

# View the report
cat output/report.md
```

## Tips
- Use descriptive chart titles and axis labels
- Save charts at reasonable resolution (dpi=100-150)
- Format large numbers with thousands separators
- Round statistics to 2 decimal places for readability
- Use colors that are colorblind-friendly
