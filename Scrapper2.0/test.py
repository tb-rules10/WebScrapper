links = []
links1 = []

file = open("sample.txt", "r")
for word in file.read().split():
    # print(word)
    if len(word) == 0: 
        continue
    links.append(word)

for link in links:
    # links1.append(link[7:])
    l = len(link)
    n = link.find(":")
    links1.append(link[n+1:])
    # if n >= 0:
    #     str = link[n+1:]
    #     links1.append(str)
    # else:
    #     links1.append(link)

for i in range(0,len(links1)):
    print(links1[i])


# mystring = "Meet Guru99 Tutorials Site.Best site for Python Tutorials!"
# print("The position of Tutorials is at:", mystring.find("Z"))
# print(mystring[0:12])
