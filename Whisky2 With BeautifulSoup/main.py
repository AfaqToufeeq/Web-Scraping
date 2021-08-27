import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

baseurl = 'https://www.thewhiskyexchange.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
productlink = []

for x in range(1,6):
    r = requests.get(f'http://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}#productlist-filter')
    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('div', class_='product-grid')


    for item in productlist:
        for link in item.find_all('a', href=True):
            #print(link['href'])
            productlink.append(baseurl + link['href'])

# print(len(productlink))

#testlink = 'https://www.thewhiskyexchange.com/p/37326/akashi-red'
whiskylist = []
for link in productlink:
    r = requests.get(link, headers=headers)
    soup=BeautifulSoup(r.content, 'lxml')
    name = soup.find('h1' ,class_='product-main__name').text.strip()
    price = soup.find('p', class_='product-action__price').text.strip()

    try:
        rating = soup.find('div', class_='review-overview').text.strip()
        reviews = soup.find('span', class_='review-overview__count').text.strip()
    except:
        rating = "No Rating"
        reviews = "No Reviews"

    whisky = {
        'name' : name,
        'rating' : rating,
        'reviews' : reviews,
        'price' : price
    }
    whiskylist.append(whisky)
    print('Saving', whisky['name'])

df = pd.DataFrame(whiskylist)
print(df.head(15))
