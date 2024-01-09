import requests
from bs4 import BeautifulSoup

url = input("Enter url: ")
name = input("Enter site name: ") + ".html"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, "lxml")
f = open(name, "x")
f.write(soup.prettify())
print(f"Done! The file is {name}")
input()