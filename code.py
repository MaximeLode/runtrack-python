import requests
from bs4 import BeautifulSoup

# Make a request to the webpage
response = requests.get('https://www.vinted.fr/catalog?search_text=jogging%20nike&currency=EUR&search_id=7725226722&order=newest_first')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the elements you want to scrape
elements = soup.find_all('a')

# Extract the data you want from the elements
for element in elements:
    link = element.get('href')
    print(link)