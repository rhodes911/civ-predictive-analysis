#!/usr/bin/env python3
"""
Comprehensive CSV Analysis Tool for Civ VI Log Files
Analyzes all CSV files in the logs directory and generates detailed documentation
"""

import pandas as pd
import os
import numpy as np
from pathlib import Path
import json
from datetime import datetime

class CivCSVAnalyzer:
    def __init__(self):
        # Path to Civ VI logs directory
        self.logs_path = Path(os.path.expandvars(r"${LOCALAPPDATA}\Firaxis Games\Sid Meier's Civilization VI\Logs"))
        self.analysis_results = {}
        self.markdown_docs = []
        
    def analyze_csv_file(self, csv_path):
        """Analyze a single CSV file and return comprehensive metadata"""
        try:
            print(f"📊 Analyzing {csv_path.name}...")
            
            # Read the CSV file
            df = pd.read_csv(csv_path)
            
            # Basic file info
            file_info = {
                'filename': csv_path.name,
                'file_size_kb': round(csv_path.stat().st_size / 1024, 2),
                'row_count': len(df),
                'column_count': len(df.columns),
                'columns': list(df.columns),
                'dtypes': {col: str(dtype) for col, dtype in df.dtypes.items()},
                'memory_usage_mb': round(df.memory_usage(deep=True).sum() / 1024 / 1024, 2)
            }
            
            # Column analysis
            column_analysis = {}
            for col in df.columns:
                col_data = {
                    'data_type': str(df[col].dtype),
                    'non_null_count': df[col].count(),
                    'null_count': df[col].isnull().sum(),
                    'unique_values': df[col].nunique(),
                }
                
                # Sample values (first 5 non-null)
                sample_values = df[col].dropna().head(5).tolist()
                col_data['sample_values'] = sample_values
                
                # For numeric columns, add statistical info
                if df[col].dtype in ['int64', 'float64']:
                    col_data['min_value'] = df[col].min() if not df[col].empty else None
                    col_data['max_value'] = df[col].max() if not df[col].empty else None
                    col_data['mean_value'] = round(df[col].mean(), 2) if not df[col].empty else None
                
                # For string columns, show value distribution if reasonable
                if df[col].dtype == 'object' and df[col].nunique() <= 20:
                    col_data['value_counts'] = df[col].value_counts().head(10).to_dict()
                
                column_analysis[col] = col_data
            
            file_info['column_analysis'] = column_analysis
            
            # Data preview (first few rows)
            file_info['data_preview'] = df.head(3).to_dict('records')
            
            return file_info
            
        except Exception as e:
            print(f"❌ Error analyzing {csv_path.name}: {str(e)}")
            return {
                'filename': csv_path.name,
                'error': str(e),
                'file_size_kb': round(csv_path.stat().st_size / 1024, 2) if csv_path.exists() else 0
            }
    
    def generate_markdown_doc(self, file_info):
        """Generate markdown documentation for a CSV file"""
        filename = file_info['filename']
        
        # Start markdown content
        md_content = f"""## {filename}

**File Statistics:**
- Size: {file_info.get('file_size_kb', 0)} KB
- Rows: {file_info.get('row_count', 0):,}
- Columns: {file_info.get('column_count', 0)}
- Memory Usage: {file_info.get('memory_usage_mb', 0)} MB

"""
        
        if 'error' in file_info:
            md_content += f"❌ **Error:** {file_info['error']}\n\n"
            return md_content
        
        # Column documentation
        md_content += "### Column Details\n\n"
        md_content += "| Column | Type | Non-Null | Unique | Sample Values | Notes |\n"
        md_content += "|--------|------|----------|--------|---------------|-------|\n"
        
        for col_name, col_data in file_info.get('column_analysis', {}).items():
            data_type = col_data.get('data_type', 'unknown')
            non_null = col_data.get('non_null_count', 0)
            unique = col_data.get('unique_values', 0)
            samples = col_data.get('sample_values', [])
            
            # Format sample values for display
            sample_str = ', '.join([str(v)[:30] for v in samples[:3]])
            if len(sample_str) > 50:
                sample_str = sample_str[:47] + "..."
            
            # Add statistical notes for numeric columns
            notes = ""
            if 'min_value' in col_data:
                notes = f"Range: {col_data['min_value']} - {col_data['max_value']}"
            elif 'value_counts' in col_data:
                top_values = list(col_data['value_counts'].keys())[:2]
                notes = f"Top: {', '.join(map(str, top_values))}"
            
            md_content += f"| `{col_name}` | {data_type} | {non_null:,} | {unique:,} | {sample_str} | {notes} |\n"
        
        # Data preview section
        if 'data_preview' in file_info and file_info['data_preview']:
            md_content += "\n### Sample Data\n\n"
            md_content += "```json\n"
            md_content += json.dumps(file_info['data_preview'][:2], indent=2, default=str)
            md_content += "\n```\n\n"
        
        # Database mapping suggestions
        md_content += "### Database Mapping Suggestions\n\n"
        md_content += f"**Recommended Table Name:** `{filename.replace('.csv', '').lower()}`\n\n"
        
        md_content += "**Column Mappings:**\n"
        for col_name, col_data in file_info.get('column_analysis', {}).items():
            data_type = col_data.get('data_type', 'unknown')
            
            # Suggest PostgreSQL data types
            if data_type == 'int64':
                pg_type = 'INTEGER'
            elif data_type == 'float64':
                pg_type = 'DECIMAL(10,2)'
            elif data_type == 'bool':
                pg_type = 'BOOLEAN'
            else:
                max_len = max([len(str(v)) for v in col_data.get('sample_values', [''])]) if col_data.get('sample_values') else 50
                pg_type = f'VARCHAR({max(max_len + 20, 100)})'
            
            md_content += f"- `{col_name}` → {pg_type}\n"
        
        md_content += "\n---\n\n"
        return md_content
    
    def analyze_all_csvs(self):
        """Analyze all CSV files in the logs directory"""
        print(f"🔍 Scanning CSV files in: {self.logs_path}")
        
        csv_files = list(self.logs_path.glob("*.csv"))
        print(f"📂 Found {len(csv_files)} CSV files")
        
        # Analyze each file
        for csv_file in sorted(csv_files):
            file_info = self.analyze_csv_file(csv_file)
            self.analysis_results[csv_file.name] = file_info
            
            # Generate markdown documentation
            md_doc = self.generate_markdown_doc(file_info)
            self.markdown_docs.append(md_doc)
        
        print(f"✅ Analysis complete for {len(csv_files)} files")
    
    def save_results(self):
        """Save analysis results to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save JSON analysis
        json_file = f"csv_analysis_{timestamp}.json"
        with open(json_file, 'w') as f:
            json.dump(self.analysis_results, f, indent=2, default=str)
        print(f"💾 Saved detailed analysis to: {json_file}")
        
        # Save markdown documentation
        md_file = f"csv_documentation_{timestamp}.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write("# Civ VI CSV Files Analysis & Documentation\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Total Files Analyzed:** {len(self.analysis_results)}\n\n")
            f.write("---\n\n")
            
            # Write all markdown docs
            for md_doc in self.markdown_docs:
                f.write(md_doc)
        
        print(f"📚 Saved markdown documentation to: {md_file}")
        
        # Generate summary statistics
        self.generate_summary()
    
    def generate_summary(self):
        """Generate and print summary statistics"""
        print("\n" + "="*60)
        print("📊 CSV ANALYSIS SUMMARY")
        print("="*60)
        
        total_files = len(self.analysis_results)
        total_size_kb = sum(info.get('file_size_kb', 0) for info in self.analysis_results.values())
        total_rows = sum(info.get('row_count', 0) for info in self.analysis_results.values())
        total_cols = sum(info.get('column_count', 0) for info in self.analysis_results.values())
        
        print(f"📂 Total Files: {total_files}")
        print(f"💾 Total Size: {total_size_kb:.1f} KB ({total_size_kb/1024:.1f} MB)")
        print(f"📊 Total Rows: {total_rows:,}")
        print(f"📋 Total Columns: {total_cols}")
        
        # Largest files
        print(f"\n🏆 LARGEST FILES:")
        largest_files = sorted(self.analysis_results.items(), 
                             key=lambda x: x[1].get('file_size_kb', 0), reverse=True)[:5]
        for filename, info in largest_files:
            size_kb = info.get('file_size_kb', 0)
            rows = info.get('row_count', 0)
            print(f"   {filename}: {size_kb:.1f} KB ({rows:,} rows)")
        
        # Most columns
        print(f"\n📋 MOST COLUMNS:")
        most_cols = sorted(self.analysis_results.items(), 
                          key=lambda x: x[1].get('column_count', 0), reverse=True)[:5]
        for filename, info in most_cols:
            cols = info.get('column_count', 0)
            print(f"   {filename}: {cols} columns")
        
        # Files with errors
        errors = {k: v for k, v in self.analysis_results.items() if 'error' in v}
        if errors:
            print(f"\n❌ FILES WITH ERRORS:")
            for filename, info in errors.items():
                print(f"   {filename}: {info['error']}")
        
        print("\n" + "="*60)

def main():
    print("🚀 Starting comprehensive CSV analysis...")
    
    analyzer = CivCSVAnalyzer()
    analyzer.analyze_all_csvs()
    analyzer.save_results()
    
    print("\n✅ Analysis complete! Check the generated files for detailed documentation.")

if __name__ == "__main__":
    main()
