import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define your get_module_prerequisites function here
def get_module_prerequisites(soup):
    # Search for the <th> element containing "Module pre-requisites"
    prereq_heading = soup.find('th', string='Module pre-requisites')
    
    if prereq_heading:
        # Get the next sibling <td> element, which contains the data
        prereq_data = prereq_heading.find_next('td').get_text(strip=True)
        
        # Return the data
        return prereq_data
    else:
        return "Module pre-requisites not found on the webpage."
    

def get_module_corequisites(soup):
        # Search for the <th> element containing "Module pre-requisites"
        prereq_heading = soup.find('th', string='Module co-requisites')
        
        if prereq_heading:
            # Get the next sibling <td> element, which contains the data
            prereq_data = prereq_heading.find_next('td').get_text(strip=True)
            
            # Return the data
            return prereq_data
        else:
            print("Module co-requisites not found on the webpage.")

# Read the CSV file into a DataFrame
df = pd.read_csv('test.csv')

# Create a new column 'prerequisites' and initialize it with None values
df['prerequisites'] = None

# Iterate through each row and process the ELE Link
for index, row in df.iterrows():
    ele_link = row['ELE Link']
    
    try:
        response = requests.get(ele_link)
        soup = BeautifulSoup(response.content, 'html.parser')
        prerequisites = get_module_prerequisites(soup)
        corequisites = get_module_corequisites(soup) 
        df.at[index, 'Prerequisites'] = prerequisites
        df.at[index, 'Coerequisites'] = corequisites
        print(f"Prerequisites for row {index}: {prerequisites}")
        print(f"Corequisites for row {index}: {corequisites}")
    except Exception as e:
        print(f"Error processing row {index}: {str(e)}")

# Save the updated DataFrame to a new CSV file
df.to_csv('test_with_prerequisites.csv', index=False)
