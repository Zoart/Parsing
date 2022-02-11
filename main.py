
import json

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


#json.dumps(a, indent=3) 
# with open('index.html', "w") as file:
#     a = r.json()
#     text = json.dumps(a, indent=6)
#     # parsed = json.loads(a) #Декодирование json в формат python
#     print(text)
    # file.write(text)

# options = Options()
#
# options.headless = True
#
# driver = webdriver.Firefox(options=options)
#
# driver.get("https://forums.newworld.com/groups/Developer/posts.json")


r = requests.get('https://forums.newworld.com/topics/groups/Developer.json?page=1')

# with open('index.html', "w") as file:
#     text = json.dumps(r.text, sort_keys=True, indent=6)
#     parsed = json.loads(text)
#     file.write(parsed)





with open("json.txt") as file:
    a = file.read()
    print(["title" in a])

# a = r.json()
# text = json.dumps(a, indent=4)
# parsed = json.loads(text)
# print(text)

# with open('json.txt', "w") as file:
#     a = r.json()
#     text = json.dumps(a, indent=4)
# #     # parsed = json.loads(a)
# #     # print(text)
#     file.write(text)
