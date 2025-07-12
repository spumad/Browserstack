from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup headless browser
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


driver.get("https://elpais.com/opinion/")


links = []
elements = driver.find_elements(By.TAG_NAME, "a")

for e in elements:
    href = e.get_attribute("href")
    if (
        href and
        href.startswith("https://elpais.com/opinion/") and
        href.endswith(".html") and
        href not in links
    ):
        links.append(href)
    if len(links) >= 5:
        break

print("Collected article links:\n")
for i, link in enumerate(links, 1):
    print(f"{i}. {link}")


titles = []

for i, link in enumerate(links, 1):
    driver.get(link)
    print(f"\n→ Visiting: {link}")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1.a_t"))
        )
        title_element = driver.find_element(By.CSS_SELECTOR, "h1.a_t")
        title = title_element.text.strip()
        titles.append(title)
        print(f"{i}. {title}")
    except Exception as e:
        print(f"Failed to extract title")
        titles.append("[No Title Found]")


driver.quit()


with open("titles.txt", "w", encoding="utf-8") as f:
    for title in titles:
        f.write(title + "\n")

print(f"\n Saved {len(titles)} titles to 'titles.txt'")
