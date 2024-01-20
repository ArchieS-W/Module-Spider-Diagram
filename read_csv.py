import pandas as pd

# Read the CSV file into a DataFrame
input_csv_file = 'module_prerequisites_data.csv'
df = pd.read_csv(input_csv_file)

# Remove duplicates based on all columns
df.drop_duplicates(inplace=True)

# Sort the DataFrame alphabetically by a specific column (e.g., 'Name')
sorted_df = df.sort_values(by='URL')
df['Module Prerequisites'] = df['Module Prerequisites'].replace("None.", None)

# Save the sorted and de-duplicated DataFrame to a new CSV file
output_csv_file = 'output.csv'
sorted_df.to_csv(output_csv_file, index=False)

print(f'Duplicates removed and data sorted alphabetically. Saved to {output_csv_file}')
