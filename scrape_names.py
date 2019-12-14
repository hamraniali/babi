import requests
from bs4 import BeautifulSoup

print("in process...")
url = "https://ooma.org/names/boys/%D8%A7%D8%B3%D9%85-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"
resp = requests.get(url)
soap = BeautifulSoup(resp.text, "html.parser")
table = soap.find("tbody")

names = ""
for td in soap.find_all("td", attrs={"class": "span2"}):
    names += td.find("a").text + "\n"

f = open("names.txt", 'w', encoding="utf8")
f.write(names)
f.close()
print("all done!")
