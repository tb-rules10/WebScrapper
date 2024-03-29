# Email Extractor

links = []
all_mails = []
counter = 0
mcounter = 0


def txt_to_list():
    try:
        file = open("all_links.txt", "r")
    except OSError as e:
        file = open("Email Extractor/all_links.txt", "r")
    for word in file.read().split():
        # print(word)
        if len(word) == 0: 
            continue
        links.append(word)


def extractMails(url):
    import requests
    from bs4 import BeautifulSoup

    try:
            r = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
            return

    global counter
    global mcounter
    counter = counter + 1
    print(counter," - ", url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    # print(soup.prettify)

    anchors = soup.find_all('a')
    for link in anchors:
        if(link.get('href') != '#'):
            Link = link.get('href')
            if isinstance(Link, str) and Link.startswith("mailto") :          
                    n = Link.find("?")     
                    if n >= 0:
                        mcounter = mcounter +1
                        print("FOUND - ",mcounter)
                        all_mails.append(Link[0:n])
                    else:
                        mcounter = mcounter +1
                        print("FOUND - ",mcounter)
                        all_mails.append(Link)
                

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
    print("Scanning:-")
    for url in links:
        extractMails(url)
    printmails()
    

main()
