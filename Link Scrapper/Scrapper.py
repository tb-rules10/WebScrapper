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
c = int(input("\nExtraction Complete  ||   Enter 0 to print output, 1 to save file & 2 for both : "))
if c==1:
    with open('links_out.txt', 'w') as f:
        for i in Links:
            f.write("%s\n" % i)
elif c==0:
    for i in Links:
        print(i)
elif c==2:
    with open('links_out.txt', 'w') as f:
        for i in Links:
            f.write("%s\n" % i)
            print(i)
else:
    print("[!] Invalid Input")
