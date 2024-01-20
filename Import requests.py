import requests
from bs4 import BeautifulSoup
import pandas as pd

def read_html(url):
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

def extract_and_parse_html_between_lines(html_content, start_line, end_line):
    # Get the HTML code between the specified lines
    html_subset = "\n".join(html_content.splitlines()[start_line-1:end_line])

    # Parse the HTML content between the specified lines using BeautifulSoup
    soup = BeautifulSoup(html_subset, 'html.parser')

    # Return the parsed soup object
    return soup

def get_urls(soup):
    # Find all anchor (a) elements
    anchor_elements = soup.find_all('a', href=True)

    # Extract and return the URLs
    urls = [anchor['href'].replace('/../..', 'https://business-school.exeter.ac.uk') for anchor in anchor_elements if anchor['href'].startswith('/../../')]
    print(urls)
    return urls


# Check if the main page is successfully fetched
def main_page_urls():
    # Specify the start and end lines for the subset (adjust these according to your HTML structure)
    start_line = 657
    end_line = 811

    # Extract and parse HTML between specified lines
    subset_soup = extract_and_parse_html_between_lines(str(main_page_soup), start_line, end_line)

    # Get URLs from the subset
    subset_urls = get_urls(subset_soup)
    
    

    # Display the extracted URLs
    return (subset_urls)

module_page = "https://business-school.exeter.ac.uk/study/undergraduate/modules/"
main_page_soup = read_html(module_page)
urls = main_page_urls()

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

# Create an empty DataFrame
df = pd.DataFrame(columns=['URL', 'Module Prerequisites'])

# Iterate through the URLs and populate the DataFrame
for url in urls:
    soup = read_html(url)
    module_prerequisites_data = get_module_prerequisites(soup)
    module_title_data = get_moudle_title(soup)
    print(module_prerequisites_data)
    if module_prerequisites_data is not None:
        df = df._append({'URL':module_title_data , 'Module Prerequisites': module_prerequisites_data}, ignore_index=True)

# Display the DataFrame
print(df)

# If you want to save the DataFrame to a CSV file
#df.to_csv('module_prerequisites_data.csv', index=False)
#print("Data stored in 'module_prerequisites_data.csv'")
