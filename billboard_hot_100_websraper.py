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

filename = 'billboard_hot_100.csv'
f = open(filename, 'w') # w = write

headers = 'Song, Artist\n'

f.write(headers)

print('Welcome to Jaimes Subroto\'s Billboard Hot 100 Python Web Scraper!')
print('Printing this week\'s HOTTEST 100 songs...')

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

    f.write(song + ',\"' + artist.replace('Featuring', 'Feat.') + '\"\n')

f.close()

print('\nWeb scraped data saved to {}'.format(filename))
print('Thank you for using Jaimes Subroto\'s Web Scraping app for Billboard HOT 100!')