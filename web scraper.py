import requests
from bs4 import BeautifulSoup

respose = requests.get ("https://books.toscrape.com/")
soup = BeautifulSoup(respose.content,"html.parser")
books = soup.find_all("article")

for book in books :
    title = book.h3.a["title"]
    rating = book.p["class" ][1]
    price = book.select('div p.price_color')[0].text.strip()
    

    print(f"Your book title is: {title} | Your book rating is: {rating} star | Your book price is: {price}£")

   

















