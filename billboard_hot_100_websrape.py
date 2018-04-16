from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as soup

url = 'https://www.billboard.com/charts/hot-100'

# Opening up connection, grabbing the page
uClient = uRequest(url)
page_html = uClient.read() # Offloads content into a variable
uClient.close() # Close the client

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grabs divs, each containing the song and artist name
containers = page_soup.findAll('div', {'class': 'chart-row__title'})

chart_position = 1

# Loops through each container
for container in containers:

    # Grabs the song name
    song = container.h2.text
    
    # Grabs the artist name
    try:
        artist = container.a.text.strip()
    except AttributeError:
        artist = container.span.text.strip()

    # Prints the chart position, song name, and artist name
    print('\nPosition: #{}'.format(chart_position))
    print('Song: {}'.format(song))
    print('Artist: {}'.format(artist))

    chart_position += 1