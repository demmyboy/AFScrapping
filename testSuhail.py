import requests
from bs4 import BeautifulSoup
import pprint
import urllib.request
import csv 

# headers = requests.utils.default_headers()
# headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
urllib._urlopener = AppURLopener()

urls = [ 
    'https://www.suhailcosmetics.com/catalog/product/view/id/13018/s/pcj-adult-relaxer-kit/',
    
    

     ]

# Save into excel sheet
file = open('pcj.csv', 'a', newline='')
writer = csv.writer(file)
# give excel a header 
writer.writerow(["Product Name", 'Brand', 'Price', 'ImageName'])


for url in urls:
    res = requests.get(url)
    data =res.content
    soup = BeautifulSoup(data, "html.parser")
    image = soup.find("meta", property="og:image").get('content').replace(" ", "")
    name = soup.find('span', class_='base').get_text().strip()
    fullImageName = name + ".jpg"
    brand = soup.select_one('tr:nth-child(2) > td:nth-child(2)').get_text().strip()
    productPrice = 40
    # write to excel sheet
    writer.writerow([name, brand, productPrice, image])

    # download the images
    urllib._urlopener.retrieve(image, fullImageName)
    pprint.pprint(f"{image} and name is {name} and brand is {brand}")
file.close()


