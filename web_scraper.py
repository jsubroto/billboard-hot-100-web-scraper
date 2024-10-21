import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Welcome to Jaimes Subroto's Billboard Hot 100 Python Web Scraper!")

while True:
    image_data = input(
        "Would you like to scrape image and status data? ")
    if image_data.lower() in {"yes", 'y'}:
        image_data = True
        break
    elif image_data.lower() in {"no", 'n'}:
        image_data = False
        break
    else:
        print("Sorry, I didn't get that.")


while True:
    print_data = input(
        "Would you like the data to be printed to the console? ")
    if print_data.lower() in {"yes", 'y'}:
        print_data = True
        print("\nPrinting this week's HOTTEST 100 songs...")
        break
    elif print_data.lower() in {"no", 'n'}:
        print_data = False
        print("\nScraping this week's HOTTEST 100 songs...")
        break
    else:
        print("Sorry, I didn't get that.")


filename = "billboard_hot_100.csv"
f = open(filename, 'w')  # w = write

headers = "Image, Status, " if image_data else ''
headers += "Song, Artist, Last Week, Peak Position, Weeks on Chart\n"

f.write(headers)

for i, container in enumerate(soup.select("ul.o-chart-results-list-row")):
    song = container.find("h3", {"class": "c-title"}).text.strip()
    artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

    last_week, peak_position, weeks_on_chart = container.find_all(
        "ul", {"class": "lrv-a-unstyle-list"})[-1].text.strip().split()

    if image_data:
        image_url = container.find(
            "img")["src"] if container.find("img") else "N/A"

        status = container.find(
            "span", {"class": "u-background-color-yellow"})
        if status:
            status_svg = f'<span>{''.join(status.text.split())}</span>'
        else:
            status_svgs = container.find_all("svg")
            status_svg = str(status_svgs[1])

    if print_data:
        print(f"\nPosition: #{i + 1}")
        print(f"Song: {song}")
        print(f"Artist: {artist}")
        print(f"Last Week: {last_week}")
        print(f"Peak Position: {peak_position}")
        print(f"Weeks on Chart: {weeks_on_chart}")

    if image_data:
        f.write(f'\"{image_url}\",\"{status_svg}\",')
    f.write(f'\"{song}\",\"{artist.replace("Featuring", "Feat.")}\",{
            last_week},{peak_position},\"{weeks_on_chart}\"\n')

f.close()

print("\nWeb scraped data saved to {}".format(filename))
print("Thank you for using Jaimes Subroto's Web Scraping app for Billboard HOT 100!")
