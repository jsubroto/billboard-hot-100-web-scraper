# Billboard Hot 100 Web Scraper  

![Billboard Logo](https://i2.wp.com/263chat.com/wp-content/uploads/2017/12/billboard-top-100.jpg?fit=1024%2C807&ssl=1)

Python application that scrapes *[Billboard's Hot 100 Chart](https://www.billboard.com/charts/hot-100)* using **BeautifulSoup**. 

The scraped data is stored in a CSV file named `billboard_hot_100.csv`.

## CSV schema

Columns:
- Image
- Song
- Artist
- Last Week
- Peak Position
- Weeks on Chart

## Installation

```bash
# clone repository
git clone https://github.com/jsubroto/billboard-hot-100-web-scraper
cd billboard-hot-100-web-scraper

# install dependencies
uv sync
```

## Run the scraper

```bash
uv run main.py
```

Output: `billboard_hot_100.csv` in the project root.

## View the CSV in a styled HTML table

`index.html` uses Tailwind (CDN) and PapaParse to render the CSV. It will:

- Auto-load `billboard_hot_100.csv` if present in the same directory.
- Fallback to a file picker so you can upload any CSV.

Steps:
```bash
# from the project directory
uv run -m http.server 3000
# then open:
localhost:3000
```

## Notes

- Browsers block file:// fetches. Serve over HTTP as above.
- The viewer expects the first CSV row to contain headers.
- Image cells: if a cell parses as a URL, it is rendered as an <img>.

## License

[MIT](LICENSE)

