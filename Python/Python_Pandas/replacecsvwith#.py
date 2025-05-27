import pandas as pd

def excel_to_custom_text(input_excel, output_txt, sheet_name=0):
    # Read the Excel file
    df = pd.read_excel(input_excel, sheet_name=sheet_name)

    # Remove completely blank rows
    df.dropna(how='all', inplace=True)

    # Remove the header row (we'll treat all rows as data)
    data = df.values.tolist()

    # Write to text file with ~#~ separator
    with open(output_txt, 'w', encoding='utf-8') as f:
        for row in data:
            # Convert all elements to string and strip whitespace
            cleaned_row = [str(item).strip() for item in row]
            # Join with custom separator and write to file
            f.write('#~#'.join(cleaned_row) + '\n')



# Example usage
input_excel = '/home/buzzadmin/Downloads/Backup/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_Pandas/testdata.xlsx'
output_txt = '/home/buzzadmin/Downloads/Backup/Documents/Desktop/Click_On_This/upload/Project-B/Python/Python_Pandas/output.txt'
excel_to_custom_text(input_excel, output_txt)
