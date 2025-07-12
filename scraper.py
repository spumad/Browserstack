from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://elpais.com/opinion/")

links = []
elements = driver.find_elements(By.TAG_NAME, "a")

for e in elements:
    href = e.get_attribute("href")
    if href and href.startswith("https://elpais.com/opinion/") and href not in links:
        links.append(href)
    if len(links) >= 5:
        break

print("Selenium collected:", links)
driver.quit()
