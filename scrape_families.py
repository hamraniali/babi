import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

print("in proccess...")
url = "http://tamadonema.ir/%D9%86%D8%A7%D9%85%E2%80%8C%D9%87%D8%A7%DB%8C-%D8%AE%D8%A7%D9%86%D9%88%D8%A7%D8%AF%DA%AF%DB%8C-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%DB%8C"
response = requests.get(url)
soap = BeautifulSoup(response.text , "html.parser")
container = soap.find("table")
families = ""

for family in container.find_all('p'):
    families += family.text

f = open("families.txt", 'w', encoding="utf8")
f.write(families)
f.close()
print("all done!")