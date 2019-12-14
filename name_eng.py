import requests
from bs4 import BeautifulSoup

url = "https://babynames.net/all/pers   ./0ian"
resp = requests.get(url)
soap = BeautifulSoup(url , "html.parser")

table = soap.find("ul" , atuitrs={"class" : 'names-result'})

print(table)