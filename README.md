# Menu Scraper

A simple Python script that scrapes the menu (item names and prices) from the [Spice Bite Fast Food](https://spice-bite-fast-food.vercel.app/) website and saves it to a CSV file.

## What It Does

1. Sends an HTTP GET request to the Spice Bite website.
2. Parses the HTML using BeautifulSoup to find all menu items (`<article class="menu-item">`).
3. Extracts each item's name and price from the "Add" button's `data-name` and `data-price` attributes.
4. Saves the results to `menu.csv`.
5. Prints the scraped menu to the console.

## Requirements

- Python 3.7+
- Packages:
  - `requests`
  - `beautifulsoup4`

Install dependencies with:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script from the command line:

```bash
python menu_scraper.py
```

If the request succeeds, a file named `menu.csv` will be created in the same directory, and the menu items will be printed to the console. If the request fails, an `Error` message will be printed instead.

## Output

The generated `menu.csv` will have the following format:

| Food        | Price |
|-------------|-------|
| Item Name 1 | 0.00  |
| Item Name 2 | 0.00  |

## Notes

- The script uses a custom `User-Agent` header to avoid being blocked by the server.
- A 10-second timeout is set on the request to prevent it from hanging indefinitely.
- If the site's HTML structure changes (e.g., different class names or attributes), the script's selectors (`menu-item`, `add-btn`, `data-name`, `data-price`) will need to be updated accordingly.
