import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_url(Modules)

def readhtml(url):
    # Fetch the HTML content of the webpage
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        return soup
    else:
        print(f"Failed to fetch webpage. Status code: {response.status_code}")
        return None
def get_module_prerequisites(soup):
        # Search for the <th> element containing "Module pre-requisites"
        prereq_heading = soup.find('th', string='Module pre-requisites')
        
        if prereq_heading:
            # Get the next sibling <td> element, which contains the data
            prereq_data = prereq_heading.find_next('td').get_text(strip=True)
            
            # Return the data
            return prereq_data
        else:
            print("Module pre-requisites not found on the webpage.")
        
def get_moudle_title(soup):
    title =soup.find("h1")
    module_title = title.get_text(strip = True)
    return module_title
            
# URLs of the webpages
urls = [
    "https://business-school.exeter.ac.uk/module/?mod_code=BEE1023&ay=2023/4&sys=0",
    # Add more URLs if needed
]

# Create an empty DataFrame
df = pd.DataFrame(columns=['URL', 'Module Prerequisites'])

# Iterate through the URLs and populate the DataFrame
for url in urls:
    soup = readhtml(url)
    module_prerequisites_data = get_module_prerequisites(soup)
    module_title_data = get_moudle_title(soup)
    if module_prerequisites_data is not None:
        df = df._append({'URL':module_title_data , 'Module Prerequisites': module_prerequisites_data}, ignore_index=True)

# Display the DataFrame
print(df)

# If you want to save the DataFrame to a CSV file
#df.to_csv('module_prerequisites_data.csv', index=False)
#print("Data stored in 'module_prerequisites_data.csv'")
