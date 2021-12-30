# Mail Mafia

links = []
all_links = set()
c=[399]

def txt_to_list():
    file = open("links_ki_versha.txt", "r")
    for word in file.read().split():
        # print(word)
        if len(word) == 0: 
            continue
        links.append(word)


def extractMails(url):
    import requests
    from bs4 import BeautifulSoup

    # c[0] += 1
    # print(c)

    try:
            r = requests.get(url)
    except requests.exceptions.RequestException as e:    # This is the correct syntax
            # print (e)
            return
    
    print(url)
    all_links.add(url)
    
    # htmlContent = r.content
    # soup = BeautifulSoup(htmlContent, 'html.parser')
    # # print(soup.prettify)

    # anchors = soup.find_all('a')
    # for link in anchors:
    #     if(link.get('href') != '#'):
    #         Link = link.get('href')
    #         print(Link)
        
            # print(type(Link))
            # if type(Link) == "<class 'str'>":
            #     if Link.startswith("mailto") is True:
            #         all_mails.add(Link)
                
        

def main():
    txt_to_list()
    for url in links:
        extractMails(url)
    # print(all_links)


main()