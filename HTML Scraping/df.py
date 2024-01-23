import pandas as pd

# Load the DataFrame from a CSV file
# Replace 'your_data_file.csv' with the path to your CSV file
data_file_path = 'updated_module_data.csv'
data = pd.read_csv(data_file_path)

# Ensure the DataFrame contains 'Module Code', 'Prerequisite_Codes', and 'Coerequisite_Codes' columns
# This step assumes these columns exist in your DataFrame. If not, adjust the column names accordingly.

# Select the columns of interest and export to a new CSV file
output_file_path = 'module_relationships.csv'
data[['Module Code', 'Prerequisites', 'Coerequisites']].to_csv(output_file_path, index=False)

print(f"CSV file has been saved to {output_file_path}")
