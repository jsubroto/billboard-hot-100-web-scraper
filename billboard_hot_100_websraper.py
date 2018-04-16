from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as soup

url = 'https://www.billboard.com/charts/hot-100'

# Opening up connection, grabbing the page
uClient = uRequest(url)
page_html = uClient.read() # Offloads content into a variable
uClient.close() # Close the client

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grabs all information related to the top 100 songs
containers = page_soup.select('article[class*=chart]') # *= means contains

filename = 'billboard_hot_100.csv'
f = open(filename, 'w') # w = write

headers = 'Song, Artist, Last Week, Peak Position, Weeks on Chart\n'

f.write(headers)

print('Welcome to Jaimes Subroto\'s Billboard Hot 100 Python Web Scraper!')
print('Printing this week\'s HOTTEST 100 songs...')

chart_position = 1

# Loops through each container
for container in containers:

    # Container storing the song name and artist name
    song_container = container.find('div', {'class': 'chart-row__title'})

    # Grabs the song name
    song = song_container.h2.text
    
    # Grabs the artist name
    try:
        artist = song_container.a.text.strip()
    except AttributeError:
        artist = song_container.span.text.strip()

    # Grabs the song's position last week
    last_week_container = container.find('div', {'class': 'chart-row__last-week'})
    last_week = last_week_container.find('span', {'class': 'chart-row__value'}).text

    # Grabs the song's peak position
    peak_position_container = container.find('div', {'class': 'chart-row__top-spot'})
    peak_position = peak_position_container.find('span', {'class': 'chart-row__value'}).text

    # Grabs the song's duration in the hot 100 (in weeks)
    weeks_on_chart_container = container.find('div', {'class': 'chart-row__weeks-on-chart'})
    weeks_on_chart = weeks_on_chart_container.find('span', {'class': 'chart-row__value'}).text

    # Prints the chart position, song name, artist name, and related stats
    print('\nPosition: #{}'.format(chart_position))
    print('Song: {}'.format(song))
    print('Artist: {}'.format(artist))
    print('Last Week: {}'.format(last_week))
    print('Peak Position: {}'.format(peak_position))
    print('Weeks on Chart: {}'.format(weeks_on_chart))

    chart_position += 1

    f.write('\"' + song + '\",\"' + artist.replace('Featuring', 'Feat.') + '\",' + last_week + ',' + peak_position + ',' + weeks_on_chart + '\n')

f.close()

print('\nWeb scraped data saved to {}'.format(filename))
print('Thank you for using Jaimes Subroto\'s Web Scraping app for Billboard HOT 100!')