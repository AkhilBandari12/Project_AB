# import pandas as pd

# # Load the Excel file
# input_file = '/home/buzzadmin/Downloads/Arrear_Sept_24.xlsx'

# df = pd.read_excel(input_file)

# # Extract relevant columns
# df = df[['ESIC LOCATION','ESINumber', 'DAYS', 'GROSS', 'Arrear Month - Remarks']]

# # Ensure 'Arrear Month - Remarks' column is treated as a string
# df['Arrear Month - Remarks'] = df['Arrear Month - Remarks'].astype(str)

# # Get unique months from the 'Arrear Month - Remarks' column
# months = df['Arrear Month - Remarks'].unique()
# locations = df['ESIC LOCATION'].unique()


# # Process each month
# for month in months:
#     # Filter data for the month
#     month_df = df[df['Arrear Month - Remarks'] == month]
#     for location in locations:
#         location_df = month_df[month_df['ESIC LOCATION'] == location]
#         if not location_df.empty:
#             location_df = location_df[['ESINumber', 'DAYS', 'GROSS']]
#             output_file = f'{location}_{month}.xlsx'
#             location_df.to_excel(output_file, index=False)
#             print(f"Saved: {output_file}")

import os
import pandas as pd

# Load the Excel file
input_file = '/home/buzzadmin/Downloads/Arrear_Sept_24.xlsx'
df = pd.read_excel(input_file)

# Extract relevant columns
df = df[['ESIC LOCATION', 'ESINumber', 'DAYS', 'GROSS', 'Arrear Month - Remarks']]

# Ensure 'Arrear Month - Remarks' column is treated as a string
df['Arrear Month - Remarks'] = df['Arrear Month - Remarks'].astype(str)

# Get unique months from the 'Arrear Month - Remarks' column
months = df['Arrear Month - Remarks'].unique()
locations = df['ESIC LOCATION'].unique()

# Process each month
for month in months:
    # Create a directory for the month if it doesn't exist
    month_dir = os.path.join('/home/buzzadmin/Documents/', month)
    os.makedirs(month_dir, exist_ok=True)

    # Filter data for the month
    month_df = df[df['Arrear Month - Remarks'] == month]

    for location in locations:
        location_df = month_df[month_df['ESIC LOCATION'] == location]
        if not location_df.empty:
            location_df = location_df[['ESINumber', 'DAYS', 'GROSS']]
            output_file = os.path.join(month_dir, f'{location}_{month}.xlsx')
            location_df.to_excel(output_file, index=False)
            print(f"Saved: {output_file}")
