from urllib.request import urlopen
from bs4 import BeautifulSoup
from clean import clean_data
import json
import re

# 🔹 Save data to JSON file
def save_data(data, filename="applicant_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f" Saved {len(data)} entries to {filename}")

# 🔹 Load data from JSON file (optional use)
def load_data(filename="applicant_data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f" Loaded {len(data)} entries from {filename}")
        return data
    except FileNotFoundError:
        print(f" File '{filename}' not found.")
        return []

# 🔹 Main scraper
def scrape_data(pages=1):
    all_results = []

    for page_num in range(1, pages + 1):
        url = f"https://www.thegradcafe.com/survey/?page={page_num}"
        print(f" Fetching: {url}")

        try:
            page = urlopen(url)
            soup = BeautifulSoup(page.read(), "html.parser")
        except Exception as e:
            print(f" Failed to fetch page {page_num}: {e}")
            continue

        table_body = soup.find("tbody")
        rows = table_body.find_all("tr") if table_body else []
        print(f" Found {len(rows)} rows in <tbody> on page {page_num}")

        i = 0
        while i < len(rows):
            row = rows[i]
            tds = row.find_all("td")

            # Identify main entry by structure: 5 tds + result link
            is_main = len(tds) == 5 and tds[-1].find("a", href=re.compile(r"^/result/"))

            if is_main:
                main_row = row
                detail_row = None

                # Check for detail row following main row
                if i + 1 < len(rows):
                    next_row = rows[i + 1]
                    if next_row.get("class") == ["tw-border-none"]:
                        detail_row = next_row
                        i += 1  # consume detail row

                # Clean and number the data
                result = clean_data(main_row, detail_row, entry_number=len(all_results) + 1)
                if result:
                    all_results.append(result)

            i += 1

    save_data(all_results)

if __name__ == "__main__":
    scrape_data(pages=15)  