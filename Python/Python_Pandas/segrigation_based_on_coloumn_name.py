import pandas as pd
import os

def split_excel_by_mandal(input_file, output_folder):
    df = pd.read_excel(input_file)
    
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Group by 'MANDAL' and save separate files
    for mandal, group in df.groupby('MANDAL'):
        file_name = f"{output_folder}/{mandal}.xlsx"
        group.to_excel(file_name, index=False)
        print(f"Saved: {file_name}")

# Example Usage
# inputpath = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_Selenium/JGTL_All_Mandals.xlsx"
inputpath = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_Selenium/RAMADUGU_2910.xlsx"
outpath = "/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/Python/Output_Excels"
split_excel_by_mandal(inputpath, outpath)
