from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import requests

# Download directory
DOWNLOAD_DIR = "../data/raw_json"

# Create folder if not exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Configure Selenium
options = Options()
options.add_argument("--headless")  # Headless mode
driver = webdriver.Chrome(options=options)

# URL to scrape
url = "https://cricsheet.org/matches/"
driver.get(url)
time.sleep(3)

# Get all match links
links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.json']")

# Download JSON files
for link in links:
    file_url = link.get_attribute("href")
    match_format = file_url.split("/")[-2]
    filename = file_url.split("/")[-1]

    format_folder = os.path.join(DOWNLOAD_DIR, match_format)
    os.makedirs(format_folder, exist_ok=True)

    file_path = os.path.join(format_folder, filename)
    
    if not os.path.exists(file_path):
        print(f"Downloading {filename}")
        response = requests.get(file_url)
        with open(file_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"{filename} already exists. Skipping...")

driver.quit()
