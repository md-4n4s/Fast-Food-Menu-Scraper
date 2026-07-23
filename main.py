import requests
from bs4 import BeautifulSoup

url = "https://spice-bite-fast-food.vercel.app/"

response = requests.get(url)

menu = {}

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="menu-item")
    for product in products:
        name = product.find("button", class_="add-btn")["data-name"]
        price = product.find("button", class_="add-btn")["data-price"]
        menu[name] = price

    for key, value in menu.items():
        print(f"{key}: {value}")

else:
    print("Error")