import requests
from bs4 import BeautifulSoup

url = "https://www.sitiowebcompetidor.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Ejemplo: Obtener nombres de productos
products = soup.find_all('h2', class_='product-name')
product_names = [product.text for product in products]

print("Productos del competidor:")
for name in product_names:
    print(f"  - {name}")
