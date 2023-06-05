import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the "Search Postings" heading
search_postings_heading = soup.find('div', class_='modal-header').find('h4')
print(search_postings_heading.text)

# Find the first 5 postings under the "Search Postings" heading
postings = soup.find_all('div', class_='postingItem')[:5]

# Extract the required fields from each posting
for posting in postings:
    est_value_notes = posting.find('span', class_='estValue').text.strip()
    description = posting.find('span', class_='description').text.strip()
    closing_date = posting.find('span', class_='closingDate').text.strip()
    
    print("Est. Value Notes:", est_value_notes)
    print("Description:", description)
    print("Closing Date:", closing_date)
    print()

