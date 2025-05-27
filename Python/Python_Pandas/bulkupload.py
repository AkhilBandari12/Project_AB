import pandas as pd
import os

def convert_excel_to_kyc_txt(input_excel_path, output_txt_path=None):
    # Step 1: Load Excel file
    try:
        df = pd.read_excel(input_excel_path, dtype=str)  # Read all values as string
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    # Step 2: Save as CSV without headers
    csv_temp_path = "temp_kyc.csv"
    try:
        df.to_csv(csv_temp_path, index=False, header=False, encoding='utf-8', lineterminator='\n')
    except Exception as e:
        print(f"Error saving temp CSV file: {e}")
        return

    # Step 3: Read CSV and replace commas with #~#
    try:
        with open(csv_temp_path, "r", encoding='utf-8') as f:
            content = f.read()
        updated_content = content.replace(",", "#~#")
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return
    finally:
        if os.path.exists(csv_temp_path):
            os.remove(csv_temp_path)  # Clean up temp file

    # Step 4: Save as TXT
    if not output_txt_path:
        output_txt_path = os.path.splitext(input_excel_path)[0] + "_bulkkyc.txt"

    try:
        with open(output_txt_path, "w", encoding='utf-8') as f:
            f.write(updated_content)
        print(f"✅ KYC text file saved at: {output_txt_path}")
    except Exception as e:
        print(f"Error saving TXT file: {e}")


# Example usage
if __name__ == "__main__":
    # Replace the filename below with your actual Excel file path
    convert_excel_to_kyc_txt("/home/buzzadmin/Downloads/Backup/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_Pandas/testdata.xlsx")
