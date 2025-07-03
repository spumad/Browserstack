import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://elpais.com/opinion/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(BASE_URL, headers=HEADERS)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
articles = []

for a in soup.find_all("a", href=True):
    href = a["href"]
    if href.startswith("https://elpais.com/opinion/") and href not in articles:
        articles.append(href)
    if len(articles) >= 5:
        break

print(f"Found {len(articles)} article links.")

titles = []
if not os.path.exists("downloads"):
    os.makedirs("downloads")

for idx, link in enumerate(articles, start=1):
    print(f"\nFetching article {idx}: {link}")
    rim = requests.get(link, headers=HEADERS)
    rim.raise_for_status()
    article_soup = BeautifulSoup(rim.text, "html.parser")

    h1 = article_soup.find("h1")
    title = h1.get_text(strip=True) if h1 else "[No title]"
    titles.append(title)
    print("Title:", title)

    
    imgage = article_soup.find("img")
    if imgage and imgage.get("src"):
        img_url = imgage["src"]
        try:
            imgage_data = requests.get(img_url).content
            with open(f"downloads/image_{idx}.jpg", "wb") as f:
                f.write(imgage_data)
            print("Downloaded image.")
        except Exception as e:
            print("Image download failed:", e)


with open("titles.txt", "w", encoding="utf-8") as f:
    for t in titles:
        f.write(t + "\n")

print(f"\n {len(titles)} titles")
