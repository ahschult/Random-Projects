# ----------------------
# Web Scraping Script
# ----------------------
# Purpose: Scrape data from a specified URL and save to a file
# Requirements: Install requests and beautifulsoup4 (pip install requests beautifulsoup4)
# Notes: Modify variables and selectors based on target website structure

# Import required libraries
import requests
from bs4 import BeautifulSoup

# ----------------------
# Configuration Section
# ----------------------
# Modify these variables for different targets
TARGET_URL = "https://example.com"  # Replace with your target URL
OUTPUT_FILE = "scraped_data.txt"     # Replace with your desired output file path
HTML_PARSER = "html.parser"         # Parser for BeautifulSoup (other options: 'lxml', 'xml')

# ----------------------
# Start Notification
# ----------------------
print("🔄 Starting web scraping process...")
print(f"🌐 Target URL: {TARGET_URL}")
print(f"💾 Output File: {OUTPUT_FILE}")

try:
    # ----------------------
    # Step 1: Send HTTP Request
    # ----------------------
    # Send GET request to target URL
    response = requests.get(TARGET_URL)
    
    # Check if request was successful (status code 200)
    response.raise_for_status()  # Raises exception for 4xx/5xx responses

    # ----------------------
    # Step 2: Parse HTML Content
    # ----------------------
    # Create BeautifulSoup object with HTML parser
    soup = BeautifulSoup(response.text, HTML_PARSER)
    
    # Example: Extract all paragraph text from the page
    # Modify the selector below based on your target website's structure
    # Common selectors: soup.find_all('tag'), soup.select('css_selector')
    scraped_data = [p.get_text(strip=True) for p in soup.find_all('p')]

    # ----------------------
    # Step 3: Save to Output File
    # ----------------------
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        for line in scraped_data:
            file.write(line + '\n')
    
    # ----------------------
    # Completion Notification
    # ----------------------
    print(f"✅ Scrape completed! {len(scraped_data)} items saved to {OUTPUT_FILE}")

except requests.exceptions.RequestException as e:
    print(f"❌ Request error: {str(e)}")
except Exception as e:
    print(f"❌ Unexpected error: {str(e)}")
finally:
    print("🏁 Web scraping process finished.")
