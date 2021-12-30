# Mail Mafia

links = []
all_mails = []


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

    try:
            r = requests.get(url)
    except requests.exceptions.RequestException as e:    # This is the correct syntax
            # print (e)
            return
    
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    # print(soup.prettify)

    anchors = soup.find_all('a')
    for link in anchors:
        if(link.get('href') != '#'):
            Link = link.get('href')
            # print(Link)
        
            # print(type(Link))
            if isinstance(Link, str):
                if Link.startswith("mailto") :
                # if Link.find("contact") :                     # For finding contact us pages
                    # if Link.startswith("mailto"):
                    #     continue
                    # elif Link.startswith("https://"):         
                    #     contact = Link
                    # else:
                    #     contact = url + Link     
                    # # n = contact.find("?")
                  
                    n = Link.find("?")                          # Replace Link with contact keyword when needed ^    
                    if n >= 0:
                        # print(Link[0:n])
                        all_mails.append(Link[0:n])
                    else:
                        # print(Link)
                        all_mails.append(Link)
                    # print(Link)
                    # all_mails.add(Link)
                
        

def main():
    txt_to_list()
    for url in links:
        extractMails(url)
    print("\n.....................................................No Errors 😎.....................................................\n")
    res = []
    for i in all_mails:
        if i not in res:
            print(i)
            res.append(i)
    # print(all_mails)


main()


