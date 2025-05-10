# scraper.py

import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"
NUM = "?p=3"


def number_of_articles(URL, NUM):
    """ This function will increase the number of articles to scrape """

    response = requests.get(URL + NUM)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        titles = soup.find_all("span", class_="titleline")

        for tag in titles:
            link = tag.find("a")  # isso pega o <a href="...">
            print(link.text, "→", link["href"])

    else:
        print("Failed to fetch the page.")   
        print("Status code:", response.status_code)
    
number_of_articles(URL, NUM)