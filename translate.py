from deep_translator import GoogleTranslator

translated = []

with open("titles.txt", "r", encoding="utf-8") as f:
    titles = f.readlines()

if not titles:
    print("titles.txt is empty. Nothing to translate.")
else:
    print(f"Found {len(titles)} titles to translate...")


for t in titles:
    try:
        translated_title = GoogleTranslator(source='auto', target='en').translate(t.strip())
        print(f"→ {translated_title}")
        translated.append(translated_title)
    except Exception as e:
        print("Translation failed:", e)
        translated.append("[Translation failed]")


with open("translated_titles.txt", "w", encoding="utf-8") as f:
    for line in translated:
        f.write(line + "\n")
