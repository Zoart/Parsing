import json

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

r = requests.get("https://forums.newworld.com/topics/groups/Developer.json?page=1")
r = r.json()
for each in r["topic_list"]["topics"]:
    print(each["title"])



# with open("topics_nw.txt", "w") as file:
#     r = r.json()
#     a = json.dumps(r, indent=3)
#     file.write(a)
