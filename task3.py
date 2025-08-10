import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

# Set headers to mimic a browser request
headers = {"User-Agent": "Mozilla/5.0"}

# Fetch the HTML content
response = requests.get(url, headers=headers)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all headlines in <h2> tags
headlines = soup.find_all("h2")

# Extract and clean text
titles = [
    h.get_text(strip=True)
    for h in headlines
    if h.get_text(strip=True)
]

# Save results to a file
with open("result.txt", "w", encoding="utf-8") as f:
    for title in titles:
        f.write(title + "\n")

print("Headlines saved to result.txt")
