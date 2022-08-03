# Email Extractor

links = []
all_mails = []


def txt_to_list():
    file = open("all_links.txt", "r")
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
    
    print("Scanning - ", url)
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
                    n = Link.find("?")                          # Replace Link with contact keyword when needed ^    
                    if n >= 0:
                        # print(Link[0:n])
                        all_mails.append(Link[0:n])
                    else:
                        # print(Link)
                        all_mails.append(Link)
                    # print(Link)
                    # all_mails.add(Link)
                

def printmails():
    res = []
    c = int(input("\nExtraction Complete  ||   Enter 0 to print output, 1 to save file & 2 for both : "))
    if c==1:
        with open('mails_out.txt', 'w') as f:    
            for i in all_mails:
                if i not in res:
                    f.write("%s\n" % i)
    elif c==0:
        for i in all_mails:
            if i not in res:
                print(i)
                res.append(i)
    elif c==2:
        with open('mails_out.txt', 'w') as f:
            for i in all_mails:
                if i not in res:
                    print(i)
                    f.write("%s\n" % i)
                    res.append(i)
    else:
        print("[!] Invalid Input")


def main():
    txt_to_list()
    for url in links:
        extractMails(url)
    printmails()
    

main()
