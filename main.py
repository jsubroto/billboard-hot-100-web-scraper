import csv

import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"


def ask_yes_no(q: str) -> bool:
    while True:
        a = input(f"{q} (y/N): ").strip().lower()
        if a in {"y", "yes"}:
            return True
        if a in {"", "n", "no"}:
            return False
        print("Invalid input, please enter y or n.")


def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    print("Welcome to Jaimes Subroto's Billboard Hot 100 Python Web Scraper!")

    is_scraping_images = ask_yes_no("Scrape image?")
    is_printing_console = ask_yes_no("Print to console?")
    mode = "Printing" if is_printing_console else "Scraping"
    print(f"\n{mode} this week's HOTTEST 100 songs...")

    filename = "billboard_hot_100.csv"
    base = ["Image"] if is_scraping_images else []
    headers = base + ["Song", "Artist", "Last Week", "Peak Position", "Weeks on Chart"]

    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        for i, container in enumerate(soup.select("ul.o-chart-results-list-row")):
            song = container.find("h3", {"class": "c-title"}).text.strip()
            artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

            stats = (
                container.find_all("ul", {"class": "lrv-a-unstyle-list"})[-1]
                .text.strip()
                .split()
            )  # ['LW', '1', 'PEAK', '1', 'WEEKS', '1']

            stats_dict = dict(zip(stats[::2], stats[1::2]))
            last_week = stats_dict.get("LW")
            peak_position = stats_dict.get("PEAK")
            weeks_on_chart = stats_dict.get("WEEKS")

            row = []
            if is_scraping_images and (img := container.find("img")):
                src = img.get("data-lazy-src") or img.get("src")
                row.append(src or "N/A")

            row += [
                song,
                artist.replace("Featuring", "Feat."),
                last_week,
                peak_position,
                weeks_on_chart,
            ]
            writer.writerow(row)

            if is_printing_console:
                for label, value in [
                    ("\nPosition", f"#{i + 1}"),
                    ("Song", song),
                    ("Artist", artist),
                    ("Last Week", last_week),
                    ("Peak Position", peak_position),
                    ("Weeks on Chart", weeks_on_chart),
                ]:
                    print(f"{label}: {value}")

    print(f"\nWeb scraped data saved to {filename}")
    print(
        "Thank you for using Jaimes Subroto's Web Scraping app for Billboard HOT 100!"
    )


if __name__ == "__main__":
    main()
