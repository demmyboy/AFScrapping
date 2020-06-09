import requests
from bs4 import BeautifulSoup
import pprint
import csv
import time


# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# Get the url 
urls = ['https://www.suhailcosmetics.com/catalog/product/view/id/11055/s/dark-natural-color-natural-black/','https://www.suhailcosmetics.com/catalog/product/view/id/11064/s/d-l-color-chestnut-blonde-380/', 
'https://www.suhailcosmetics.com/catalog/product/view/id/11063/s/d-l-color-golden-bronze-379/','https://www.suhailcosmetics.com/catalog/product/view/id/11066/s/d-l-color-lt-golden-blonde-384/','https://www.suhailcosmetics.com/catalog/product/view/id/11067/s/d-l-color-brown-sugar-386/'
 'https://www.suhailcosmetics.com/catalog/product/view/id/11068/s/d-l-color-cinnamon-391/', 'https://www.suhailcosmetics.com/catalog/product/view/id/11071/s/d-l-reviving-color-391-radiant-black/'
 ]

# Save the name and brand in excel sheet 
file = open('darkLovely.csv', 'w', newline='')
writer = csv.writer(file)
#give excel an header
writer.writerow(['Product Name', 'Brand', 'Price'])

for url in urls:
    res = requests.get(url, headers)
    time.sleep(20)
    soup = BeautifulSoup(res.text, 'html.parser')
    # Scrap the name and brand
    
    name = soup.find('span', class_='base').get_text().strip()
    brand = soup.select_one('tr:nth-child(2) > td:nth-child(2)').get_text().strip()
    
    productPhoto = soup.select_one('a > img')

    removeQuotes = name.replace("'", " ")
    productPrice = 60
     # Scrap the image and save with name
    # productFoto= soup.select('div > .fotorama__stage__shaft')
    # pprint.pprint(productFoto)
    
    pprint.pprint(f"The pictures on this {url} is {productPhoto}")
    # pprint.pprint(f"The names of the product is: {removeQuotes} and the brand is: {brand}")
    writer.writerow([removeQuotes, brand, productPrice])

   

file.close()

# Scrap the image and save with name


