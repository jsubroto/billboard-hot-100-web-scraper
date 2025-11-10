# Billboard Hot 100 Web Scraper  

![Billboard Logo](https://i2.wp.com/263chat.com/wp-content/uploads/2017/12/billboard-top-100.jpg?fit=1024%2C807&ssl=1)

Python application that scrapes [**Billboard’s Hot 100 Chart**](https://www.billboard.com/charts/hot-100) using **BeautifulSoup**, then exports the data to a CSV file and visualizes it in a Tailwind-powered web viewer.

🔗 **Live Viewer:** [GitHub Pages Demo](https://jsubroto.github.io/billboard-hot-100-web-scraper/)

---

## 📊 CSV Schema

| Column | Description |
| ------ | ----------- |
| Image | Album artwork URL |
| Song | Song title |
| Artist | Artist or group |
| Last Week | Previous chart position |
| Peak | Highest chart position reached |
| Weeks | Number of weeks on chart |

---

## 🐍 Run the Scraper

```bash
# clone repository
git clone https://github.com/jsubroto/billboard-hot-100-web-scraper
cd billboard-hot-100-web-scraper

# install dependencies
uv sync

# run the scraper
uv run main.py
```

This will generate `billboard_hot_100.csv` in the project root.

---

## 💻 View the Results

### Option 1 – Online (GitHub Pages)
The latest scraped CSV is rendered automatically here:  
👉 [**Live Billboard Hot 100 Viewer**](https://jsubroto.github.io/billboard-hot-100-web-scraper/)

### Option 2 – Local Development
Serve locally to test your own CSV:
```bash
uv run -m http.server 3000 -d docs
```
Then open [http://localhost:3000](http://localhost:3000)

> The viewer uses PapaParse to read the CSV and Tailwind for styling.  
> If no local `billboard_hot_100.csv` is found, you can upload one manually.

---

## 📝 Notes

- The web viewer automatically displays album art, song, artist, and chart stats in a Billboard-style layout.  
- Works with the generated CSV or any file following the same schema.  
- For browser security reasons, fetching local files requires serving via HTTP (not `file://`).

---

## 🪪 License

[MIT](LICENSE)
