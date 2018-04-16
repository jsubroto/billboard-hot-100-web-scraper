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

# Asks the user if he/she wants the data to be printed to the console
while True:
    print_data = input('Would you like the data to be printed to the console? ')
    if print_data.lower() == 'yes' or print_data.lower() == 'y':
        print_data = True
        print('\nPrinting this week\'s HOTTEST 100 songs...')
        break
    elif print_data.lower() == 'no' or print_data.lower() == 'n':
        print_data = False
        print('\nScraping this week\'s HOTTEST 100 songs...')
        break
    else:
        print('Sorry, I didn\'t get that.')

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
    if print_data:
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