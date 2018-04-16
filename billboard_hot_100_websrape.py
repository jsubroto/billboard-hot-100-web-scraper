from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as soup

url = 'https://www.billboard.com/charts/hot-100'

# Opening up connection, grabbing the page
uClient = uRequest(url)
page_html = uClient.read() # Offloads content into a variable
uClient.close() # Close the client

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Prints the HTML contents
print(page_soup)

# Grabs divs, each containing the song and artist name
containers = page_soup.findAll('div', {'class': 'chart-row__title'})

# Prints the length of containers
print(len(containers)) # 100