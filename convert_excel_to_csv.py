#!/usr/bin/env python3
"""
Convert Excel files to CSV format
"""
import pandas as pd
import os

def convert_excel_to_csv(excel_file, output_dir=None):
    """Convert Excel file to CSV, handling multiple sheets if present"""
    if not os.path.exists(excel_file):
        print(f"Error: File {excel_file} not found")
        return
    
    if output_dir is None:
        output_dir = os.path.dirname(excel_file)
    
    # Read the Excel file
    try:
        # First, check how many sheets are in the file
        xl_file = pd.ExcelFile(excel_file)
        sheet_names = xl_file.sheet_names
        
        print(f"Found {len(sheet_names)} sheet(s) in {excel_file}")
        
        base_name = os.path.splitext(os.path.basename(excel_file))[0]
        
        if len(sheet_names) == 1:
            # Single sheet - convert directly
            df = pd.read_excel(excel_file)
            csv_filename = os.path.join(output_dir, f"{base_name}.csv")
            df.to_csv(csv_filename, index=False)
            print(f"Converted to: {csv_filename}")
        else:
            # Multiple sheets - create separate CSV files
            for sheet_name in sheet_names:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                csv_filename = os.path.join(output_dir, f"{base_name}_{sheet_name}.csv")
                df.to_csv(csv_filename, index=False)
                print(f"Converted sheet '{sheet_name}' to: {csv_filename}")
                
    except Exception as e:
        print(f"Error converting {excel_file}: {str(e)}")

def main():
    # Convert both Excel files
    excel_files = [
        "PE4MOVE_6MWT.xlsx",
        "PE4MOVE_legends.xlsx"
    ]
    
    for excel_file in excel_files:
        if os.path.exists(excel_file):
            print(f"\nConverting {excel_file}...")
            convert_excel_to_csv(excel_file)
        else:
            print(f"Warning: {excel_file} not found")

if __name__ == "__main__":
    main()