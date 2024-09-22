import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url)

# HTML parsing
soup = BeautifulSoup(response.text, "html.parser")

# Grabs all information related to the top 100 songs
list_class = "ul.o-chart-results-list-row"
containers = soup.select(list_class)

filename = "billboard_hot_100.csv"
f = open(filename, 'w')  # w = write

headers = "Song, Artist, Last Week, Peak Position, Weeks on Chart\n"

f.write(headers)

print("Welcome to Jaimes Subroto's Billboard Hot 100 Python Web Scraper!")

# Asks the user if he/she wants the data to be printed to the console
while True:
    print_data = input(
        "Would you like the data to be printed to the console? ")
    if print_data.lower() == "yes" or print_data.lower() == 'y':
        print_data = True
        print("\nPrinting this week's HOTTEST 100 songs...")
        break
    elif print_data.lower() == "no" or print_data.lower() == 'n':
        print_data = False
        print("\nScraping this week's HOTTEST 100 songs...")
        break
    else:
        print("Sorry, I didn't get that.")

chart_position = 1

# Loops through each container
for container in containers:
    song = container.find("h3", {"class": "c-title"}).text.strip()
    artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

    last_week, peak_position, weeks_on_chart = container.find_all(
        "ul", {"class": "lrv-a-unstyle-list"})[-1].text.strip().split()

    # Prints the chart position, song name, artist name, and related stats
    if print_data:
        print("\nPosition: #{}".format(chart_position))
        print("Song: {}".format(song))
        print("Artist: {}".format(artist))
        print("Last Week: {}".format(last_week))
        print("Peak Position: {}".format(peak_position))
        print("Weeks on Chart: {}".format(weeks_on_chart))

    chart_position += 1

    f.write('\"' + song + '\",\"' + artist.replace("Featuring", "Feat.") +
            '\",' + last_week + ',' + peak_position + ',' + weeks_on_chart + '\n')

f.close()

print("\nWeb scraped data saved to {}".format(filename))
print("Thank you for using Jaimes Subroto's Web Scraping app for Billboard HOT 100!")
