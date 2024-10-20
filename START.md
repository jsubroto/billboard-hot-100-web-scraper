# Steps to Set Up a Local Server:

1. Open a terminal or command prompt.

2. Navigate to the directory where your HTML file and `billboard_hot_100.csv` are located.

   For example, if they are in `C:\your_directory`:

   ```bash
   cd C:\your_directory
   ```

3. Start a simple local HTTP server:

   If you're using Python 3.x, run:

   ```bash
   python -m http.server 8000
   ```

4. Access your HTML file in a browser by visiting:

   ```bash
   http://localhost:8000/your_html_file.html
   ```

   Replace `your_html_file.html` with the actual name of your HTML file.

## Why This Works:

- When you open an HTML file directly (e.g., by double-clicking), it uses the `file://` protocol, which restricts access to local files for security reasons.
- Running a local server allows you to access your files via `http://`, which the browser allows to fetch other files in the same directory.
