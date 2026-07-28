import requests
from bs4 import BeautifulSoup
import csv

url = "https://spice-bite-fast-food.vercel.app/"

# Identify the client making the request
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url,headers=headers,timeout=10)

menu = {}

# If request was successful
if response.status_code == 200:
    
    # Parse html content of the webpage
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all <article> with class "menu-item" 
    products = soup.find_all("article", class_="menu-item")

    # Open or create menu.csv file in write mode
    with open('menu.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object to write
        writer = csv.writer(csvfile)
        writer.writerow(["Food","Price"])

        for product in products:
            # data-name and data-price are attributes of tag
            name = product.find("button", class_="add-btn")["data-name"].strip()
            price = product.find("button", class_="add-btn")["data-price"]
            menu[name] = price

            writer.writerow([name, price])

        for key, value in menu.items():
            print(f"{key}: {value}")

else:
    print("Error")
