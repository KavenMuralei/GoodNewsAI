from bs4 import BeautifulSoup as btfs
from article import Article
import requests, re

html = requests.get("https://news.yahoo.com/").text
soup = btfs(html,"html.parser")

article = [Article] 

headlines = soup.find_all("h3")
headlines = headlines[12:len(headlines)-3]

headline_titles = []
print(headlines[0])
for headline in headlines:
    headline = str(headline)
    match = re.search(r'>([^<]+)<', headline)
    title = match.group(1)
    headline_titles.append(title)
for headline in headline_titles:
    print(headline)
