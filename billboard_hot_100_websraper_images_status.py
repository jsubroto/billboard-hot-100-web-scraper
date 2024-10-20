import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

filename = "billboard_hot_100.csv"
f = open(filename, 'w')  # w = write

# Include Award in headers
headers = "Image, Status, Song, Artist, Last Week, Peak Position, Weeks on Chart\n"
f.write(headers)

print("Welcome to Jaimes Subroto's Billboard Hot 100 Python Web Scraper!")

while True:
    print_data = input("Would you like the data to be printed to the console? ")
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

for i, container in enumerate(soup.select("ul.o-chart-results-list-row")):
    song = container.find("h3", {"class": "c-title"}).text.strip()
    artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

    last_week, peak_position, weeks_on_chart = container.find_all(
        "ul", {"class": "lrv-a-unstyle-list"})[-1].text.strip().split()

    # Get the image URL from the img element
    image_url = container.find("img")["src"] if container.find("img") else "N/A"

    # Attempt to get the award SVG
    # award_svgs = container.find_all("svg")  # Replace with actual class or ID
    # if (len(award_svgs) > 2):
    #     award_svg_url = award_svgs[3] #award_svg["src"] if award_svg else "N/A"  # Modify based on actual SVG attributes
    # else:
    #     award_svg_url = "N/A"
    new_span = container.find_all("span", {"class": "u-background-color-yellow"})
    # print(len(new_span))
    if len(new_span) > 0:
        # print(new_span[0].text.strip())
        new_text = new_span[0].text.strip()
        if new_text.endswith("ENTRY"):
            new_text = "RE-ENTRY"
            status_svg_url = f'<span style="font-family: \'Arial\', sans-serif; font-weight: bold; font-size: 0.8rem; color: #4a4a4a; background-color: #ffeb3b; text-align: center; padding: 10px">{new_text}</span>'
        else:
            status_svg_url = f'<span style="font-family: \'Arial\', sans-serif; font-weight: bold; font-size: 1.5rem; color: #4a4a4a; background-color: #ffeb3b; text-align: center; padding: 10px">{new_text}</span>'

    else:
        status_svgs = container.find_all("svg")  # Replace with actual class or ID
        status_svg_url = status_svgs[1] #award_svg["src"] if award_svg else "N/A"  # Modify based on actual SVG attributes

    if print_data:
        print(f"\nPosition: #{i + 1}")
        print(f"Song: {song}")
        print(f"Artist: {artist}")
        print(f"Last Week: {last_week}")
        print(f"Peak Position: {peak_position}")
        print(f"Weeks on Chart: {weeks_on_chart}")
        print(f"Image URL: {image_url}")
        print(f"Status SVG: {status_svg_url}")

    # Write data including image URL and Award SVG to the CSV file
    f.write(f'\"{image_url}\",\"{status_svg_url}\",\"{song}\",\"{artist.replace("Featuring", "Feat.")}\",{last_week},{peak_position},\"{weeks_on_chart}\"\n')

f.close()

print("\nWeb scraped data saved to {}".format(filename))
print("Thank you for using Jaimes Subroto's Web Scraping app for Billboard HOT 100!")
