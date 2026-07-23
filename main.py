import requests
from bs4 import BeautifulSoup
import csv

url = "https://spice-bite-fast-food.vercel.app/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url,headers=headers,timeout=10)

menu = {}

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="menu-item")

    with open('menu.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Food","Price"])

        for product in products:
            name = product.find("button", class_="add-btn")["data-name"].strip()
            price = product.find("button", class_="add-btn")["data-price"]
            menu[name] = price

            writer.writerow([name, price])

        for key, value in menu.items():
            print(f"{key}: {value}")

else:
    print("Error")