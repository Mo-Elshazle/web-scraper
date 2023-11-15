import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Unable to retrieve content. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        rating = book.select_one('p[class^="star-rating"]')['class'][1]
        price = book.select_one('p.price_color').get_text(strip=True).strip('Â£')
        print(f'Title: {title} | Rating: {rating} | Price: {price} £')


scrape_books(url)
