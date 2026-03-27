from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import zipfile
import shutil

DOWNLOAD_DIR = os.path.abspath("C:/Users/gayat/AppData/Local/Programs/Python/Python313")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://cricsheet.org/matches/")

wait = WebDriverWait(driver, 30)

zip_files = [
    "tests_json.zip",
    "odis_json.zip",
    "t20s_json.zip",
    "ipl_json.zip"
]

# Step 1: Delete old ZIP files BEFORE downloading
for zip_name in zip_files:
    zip_path = os.path.join(DOWNLOAD_DIR, zip_name)
    
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"Deleted old ZIP: {zip_name}")

# Step 2: Download fresh ZIP files
for zip_name in zip_files:
    print(f"Downloading {zip_name}...")
    
    link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//a[contains(@href, '{zip_name}')]")
        )
    )
    driver.execute_script("arguments[0].click();", link)
    time.sleep(8)

driver.quit()
print("Downloads completed.")

# Step 3: Wait for downloads to finish
def wait_for_downloads(folder):
    while any(fname.endswith(".crdownload") for fname in os.listdir(folder)):
        time.sleep(2)

wait_for_downloads(DOWNLOAD_DIR)

# Step 4: Extract and REPLACE folders
for zip_name in zip_files:
    zip_path = os.path.join(DOWNLOAD_DIR, zip_name)
    extract_folder = os.path.join(DOWNLOAD_DIR, zip_name.replace(".zip", ""))

    # ❗ Delete old extracted folder if exists
    if os.path.exists(extract_folder):
        shutil.rmtree(extract_folder)
        print(f"Deleted old folder: {extract_folder}")

    print(f"Extracting {zip_name}...")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

print("All files replaced and extracted successfully!")
