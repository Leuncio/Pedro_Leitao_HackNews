import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/?p="
NUM = 1

def number_of_articles(URL, NUM):
    """This function scrapes article titles and links from Hacker News pages."""
    list_of_articles = []

    for i in range(1, NUM + 1):  # começa em 1 porque ?p=0 não existe
        response = requests.get(URL + str(i))

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            titles = soup.find_all("span", class_="titleline")

            for tag in titles:
                link = tag.find("a")
                if link:
                    title = link.text
                    href = link["href"]
                    list_of_articles.append((title, href))
        else:
            print(f"Failed to fetch page {i} - Status code: {response.status_code}")

    return list_of_articles


articles = number_of_articles(URL, NUM)
for title, href in articles:
    print(title, "→", href)
