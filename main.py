import csv
from shutil import copyfile

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
    headers = base + ["Song", "Artist", "Last Week", "Peak", "Weeks"]

    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        rows = soup.select("ul.o-chart-results-list-row")
        for i, container in enumerate(rows, 1):
            song = container.find("h3", class_="c-title").text.strip()
            artist = container.find("span", class_="a-no-trucate").text.strip()

            stats = (
                container.find_all("ul", class_="lrv-a-unstyle-list")[-1]
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
                print(
                    f"\n#{i}: {song} — {artist}\n"
                    f"  Last Week: {last_week}\n"
                    f"  Peak: {peak_position}\n"
                    f"  Weeks: {weeks_on_chart}"
                )

    print(f"\nWeb scraped data saved to {filename}")
    copyfile(filename, f"docs/{filename}")
    print("Copied CSV to docs/ for GitHub Pages")
    print("Thanks for using Jaimes Subroto's Billboard HOT 100 Web Scraper!")


if __name__ == "__main__":
    main()
