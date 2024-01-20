import csv
from bs4 import BeautifulSoup
import re

# Open the input text file and CSV file for writing
with open('html.txt', 'r') as txtfile, open('test.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    csv_writer = csv.writer(csvfile)
    
    # Write the header row to the CSV file
    csv_writer.writerow(['Module Code', 'Module Title', 'Credits', 'Term', 'ELE Link'])
    
    # Iterate through the lines in the text file
    for line in txtfile:
        # Parse the line as HTML using BeautifulSoup
        soup = BeautifulSoup(line, 'html.parser')
        
        # Find the <a> element with href attribute
        a_tag = soup.find('a', href=True)
        
        if a_tag:
            # Extract module code, module title, credits, and term
            module_code = a_tag['href'].split('=')[1].split('&')[0]
            module_title = a_tag.text
            credits = soup.find_all('td')[1].text
            term = soup.find_all('td', class_='nowrap')[0].text
            
            # Find the ELE link, if it exists
            ele_link_element = soup.find('a', href=True, text=re.compile(r'on ELE'))
            ele_link = ele_link_element['href'] if ele_link_element else ''
            
            # Write the extracted data to the CSV file
            csv_writer.writerow([module_code, module_title, credits, term, ele_link])

print("Data extraction and CSV writing completed.")
