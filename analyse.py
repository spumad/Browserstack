from collections import Counter
import re

with open("translated_titles.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

words = []
for line in lines:
    words += re.findall(r'\b\w+\b', line.lower())  

counted = Counter(words)

print("Words that are repeating more than once:\n")
for word, count in counted.items():
    if count > 1:
        print(f"{word}: {count}")
