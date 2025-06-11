import pandas as pd                            # Import pandas


df = pd.read_csv('file.csv')                   # Read CSV
df = pd.read_excel('file.xlsx')                # Read Excel
df = pd.DataFrame(data)                        # Create DataFrame from dict/list

df.head()                                      # First 5 rows
df.tail()                                      # Last 5 rows
df.shape                                       # (rows, columns)
df.info()                                      # Summary of DataFrame
df.describe()                                  # Statistical summary
df.columns                                     # List of column names
df.index                                       # Index of DataFrame

df['column']                                   # Select single column
df[['col1', 'col2']]                           # Select multiple columns
df.loc[2]                                      # Row with label/index 2
df.iloc[2]                                     # Row at position 2
df.loc[2, 'col1']                              # Cell by label
df.iloc[2, 1]                                  # Cell by position
df.loc[1:3, ['col1', 'col2']]                  # Row and column slice by label
df.iloc[1:4, 0:2]                              # Row and column slice by position


df[df['Age'] > 30]                             # Filter rows
df[(df['Age'] > 30) & (df['Gender'] == 'M')]   # Multiple conditions
df.query('Age > 30 and Gender == "M"')         # Query-style filtering



df['new_col'] = df['col1'] + df['col2']        # Add new column
df['Age'] = df['Age'] + 1                      # Modify existing column
df.rename(columns={'old': 'new'}, inplace=True)# Rename columns
df.drop('col1', axis=1)                        # Drop column
df.drop(4, axis=0)                             # Drop row by index
df.drop(df.index[4])                           # Drop 5th row (by position)
df.insert(1, 'new', values)                    # Insert column at position



df.isnull()                                    # Check for NaNs
df.notnull()                                   # Non-null check
df.dropna()                                    # Drop rows with NaNs
df.fillna(0)                                   # Fill NaNs with 0
df.fillna(method='ffill')                      # Forward fill



df.mean()                                      # Mean
df.median()                                    # Median
df.sum()                                       # Sum
df.min()                                       # Min
df.max()                                       # Max
df.count()                                     # Count non-NaN
df['col'].value_counts()                       # Unique value count
df.groupby('Gender').mean()                    # Group by and aggregate



df.sort_values('Age')                          # Sort by column
df.sort_values(['Age', 'Name'], ascending=[1, 0])
df.sort_index()                                # Sort by index



pd.concat([df1, df2])                          # Concatenate DataFrames (vertically)
pd.merge(df1, df2, on='ID')                    # Merge on common column
df1.join(df2, lsuffix='_left', rsuffix='_right')  # Join by index


df.reset_index(drop=True)                      # Reset index
df.set_index('column')                         # Set column as index


df.to_csv('output.csv', index=False)           # Save to CSV
df.to_excel('output.xlsx', index=False)        # Save to Excel


df['col'].apply(lambda x: x*2)                 # Apply function to column
df.applymap(str)                               # Apply to entire DataFrame
df['col'].map({'M': 'Male', 'F': 'Female'})    # Map values


df.duplicated()                                # Check for duplicates
df.drop_duplicates()                           # Remove duplicates
df['col'].unique()                             # Unique values in a column
df['col'].nunique()                            # Count of unique values
