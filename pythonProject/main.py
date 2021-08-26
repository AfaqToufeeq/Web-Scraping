# If you want to scrape a website:
# Use the API
# HTML Web Scraping using some tool like bs4
# Install all the requirements
# pip install requests
# pip install html5lib
# pip install bs4


import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

#get the html
content = requests.get(url)
htmlContent = content.content
#print(htmlContent)

#Parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#Traverse the Tree
#Commonly Used type of objects:
#1. Tag
#2. NavigableString
#3. BeauftifulSoup
#4. Comment

# title = soup.title
# print(type(soup))
# print (type(title))
# print(type(title.string))


#GET THE TITLE OF HTML PAGE
title = soup.title

#GET THE PARAS FROM THE PAGE
paras= soup.find_all('p')
# print(paras)

#GET THE anchor FROM THE PAGE
anchors= soup.find_all('a')
#print(anchors)

#Get First Element in the HTML Page
#print(soup.find('p'))

#Get class of any element in the HTML Page
#print(soup.find('p')['class'])

#find all the elements with the class lead
#print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# To get the all the text from Html
# print(soup.get_text())

# To get the all the links from HTML
all_links = set()
for links in anchors:
    if(links.get('href') != '#'):
        linksText="https://codewithharry.com" +links.get('href')
        all_links.add(links)
        # print(linksText)

#4. Comments
markup = "<p><!--this is my Comment--></p>"
# soup2 = BeautifulSoup (markup)
#print(soup2.p.string)
#print(type(soup2.p.string))

navbarSupportedContent = soup.find(id='navbarSupportedContent')
#print(navbarSupportedContent.contents)
# for elem in navbarSupportedContent.contents:
#     print(elem)

# for elem in navbarSupportedContent.strings:
#     print(elem)
# for elem in navbarSupportedContent.stripped_strings:
#     print(elem)

#Get the Parent
# for elem in navbarSupportedContent.parents:
#     print(elem.name)

# print(navbarSupportedContent.next_sibling)
# print(navbarSupportedContent.previous_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('#  loginModal')
print(elem)





