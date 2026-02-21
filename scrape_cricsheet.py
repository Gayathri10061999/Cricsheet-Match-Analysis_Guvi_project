from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import zipfile

DOWNLOAD_DIR = os.path.abspath("C:/Users/gayat/cricsheet_data")
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

zip_files = {
    "tests_json.zip": "tests",
    "odis_json.zip": "odis",
    "t20s_json.zip": "t20s",
    "ipl_json.zip": "ipl"
}

for zip_name, folder in zip_files.items():
    print(f"Downloading {zip_name}...")
    
    link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//a[contains(@href, '{zip_name}')]")
        )
    )
    driver.execute_script("arguments[0].click();", link)
    time.sleep(5)

driver.quit()
print("ZIP downloads triggered.")
