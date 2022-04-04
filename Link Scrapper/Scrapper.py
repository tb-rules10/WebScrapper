# Link Scrapper

import requests
from bs4 import BeautifulSoup
url = "https://hackbmu.tech/"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# # Get the title of html page
# title = soup.title
# # print(title)

# # Get all paras from the page
# paras = soup.find_all('p')
# print(paras)
 
# print(soup.find('p'))                       # First element 
# print(soup.find('p')['class'])              # Get classes
# print(soup.find_all("p", class_="lead"))    # Find elements of a specific class
# print(soup.find('p').get_text())            # Get text
# print(soup.get_text())

# Get all anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)

# Get all the links on a page
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        Link = link.get('href')
        # print(type(Link))
        all_links.add(Link)
        # print(Link)

# Filtering the links found
Links = set()
for link in all_links:
    if link != None:
         if link.startswith("http"):
              Links.add(link)

# Printing 
for i in Links:
    print(i)
