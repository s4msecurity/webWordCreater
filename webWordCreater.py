import requests
from bs4 import BeautifulSoup
import re

print("""
               _ __          __           _  _____                _            
              | |\ \        / /          | |/ ____|              | |           
 __      _____| |_\ \  /\  / /__  _ __ __| | |     _ __ ___  __ _| |_ ___ _ __ 
 \ \ /\ / / _ \ '_ \ \/  \/ / _ \| '__/ _` | |    | '__/ _ \/ _` | __/ _ \ '__|
  \ V  V /  __/ |_) \  /\  / (_) | | | (_| | |____| | |  __/ (_| | ||  __/ |   
   \_/\_/ \___|_.__/ \/  \/ \___/|_|  \__,_|\_____|_|  \___|\__,_|\__\___|_|                                                                                                                                                              

""")


webUrl = input("Enter to WEB Page for wordlist [For example: https://www.text.com]: ")
tag4Word = input("Enter to which want you between html tag and html tag of finish for words [For example: p, body, div etc.]: ")

print("[!] Starting create wordlist.txt")

htmlSource = requests.get(webUrl)
html = BeautifulSoup(htmlSource.text, "html.parser")
desc = ''

for data in html.find_all(tag4Word):
        desc = desc + data.getText()        

text = desc.strip().split()
max = int(len(text))

i = 1
for wrd in text:
    
    newWord = re.sub('[^a-zA-Z0-9 \n\.]', '',wrd)
    if len(newWord) >= 1:
        newWord = newWord.replace(".","")
        with open("wordlist.txt", "a", encoding="utf-8") as f:            
            f.write(newWord+"\n")                    
            print("[!] Write file: "+str(i)+"/"+str(max),end="\r")
            i = i + 1    

f.close()
print("[+] Successfully Writed: "+str(i)+"/"+str(max))        
print("[+] Wordlist Ready")