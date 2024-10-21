# Billboard Hot 100 Web Scraper

![Billboard Logo](https://i2.wp.com/263chat.com/wp-content/uploads/2017/12/billboard-top-100.jpg?fit=1024%2C807&ssl=1)

  

Python application which web scrapes *[Billboard's Hot 100 Chart](https://www.billboard.com/charts/hot-100)* using **BeautifulSoup**.

  

The web scraped song informations are then stored to a .csv file named billboard\_hot\_100.csv.

  

filename = 'billboard_hot_100.csv'

  

#### .csv Headers:

* Song name

* Artist name

* Last week position

* Peak position

* Weeks on chart

* Image URL

* Status SVG

  

# Using the display_csv.html
- When you open an HTML file directly (e.g., by double-clicking), it uses the `file://` protocol, which restricts access to local files for security reasons.

- Running a local server allows you to access your files via `http://`, which the browser allows to fetch other files in the same directory.

 - Using the local server is not at all required, it is just more convenient as you don't have to upload the file manually everytime you refresh.

## Steps to Set Up a Local Server:

  

1. Open a terminal or command prompt and navigate to the directory with the csv file and html file

3. Start a simple local HTTP server:

  

If you're using Python 3.x, run:

```bash

python -m http.server 8000

```
If you're having cahcing issues (The data isn't updating) run:

```bash

python start_server.py

```

4. Access your HTML file in a browser by visiting:

  

```bash

http://localhost:8000/

```
