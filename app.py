import requests
from bs4 import BeautifulSoup
import pprint
import csv
import time
from selenium import webdriver
import urllib.request

# # Set headers
# headers = requests.utils.default_headers()
# headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"
urllib._urlopener = AppURLopener()

browser = webdriver.Chrome('C:\\Users\\demmy\\Downloads\\chromedriver_win32\\chromedriver.exe')

# List of url to scrap 
urls = ['https://www.suhailcosmetics.com/catalog/product/view/id/11055/s/dark-natural-color-natural-black/','https://www.suhailcosmetics.com/catalog/product/view/id/11064/s/d-l-color-chestnut-blonde-380/', 
'https://www.suhailcosmetics.com/catalog/product/view/id/11063/s/d-l-color-golden-bronze-379/','https://www.suhailcosmetics.com/catalog/product/view/id/11066/s/d-l-color-lt-golden-blonde-384/','https://www.suhailcosmetics.com/catalog/product/view/id/11067/s/d-l-color-brown-sugar-386/'
 'https://www.suhailcosmetics.com/catalog/product/view/id/11068/s/d-l-color-cinnamon-391/', 'https://www.suhailcosmetics.com/catalog/product/view/id/11071/s/d-l-reviving-color-391-radiant-black/'
 ]

# comicUrl = 'https://www.suhailcosmetics.com/catalog/product/view/id/11055/s/dark-natural-color-natural-black/'

# Save the name and brand in excel sheet 
file = open('darkLovely.csv', 'w', newline='')
writer = csv.writer(file)
#give excel an header
writer.writerow(['Product Name', 'Brand','Price', 'Image'])

for url in urls:
    browser.get(url)
    browser.maximize_window()
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    #added a wait to this to slow it down 
    time.sleep(10)
    images = soup.findAll('img')[1].get('src')
    imagesName = soup.find('span', class_='base').get_text().strip()
    fullName = imagesName + ".jpg"
    print(f"******THIS IS GOING TO CAUSE ERROR!*****\n ----- {images} \n ----- {fullName}")
    time.sleep(10)
    urllib._urlopener.retrieve(images, fullName)

    name = soup.find('span', class_='base').get_text().strip()
    productPrice = 60
    brand = soup.select_one('tr:nth-child(2) > td:nth-child(2)').get_text().strip()
    pprint.pprint(f"{images} is named {name} and brand is {brand}") 
    #write to excel sheet 
    writer.writerow([name, brand, productPrice, images])
file.close()

browser.close()


# #to-do
# # save the images into a folder 
# # save the name of images a s name of product 




