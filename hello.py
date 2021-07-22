import requests
from bs4 import BeautifulSoup

link = "https://codeforces.com/profile/Silvana_Prevails"
response = requests.get(link).text
with open("out.html", "w", encoding="utf8") as f:
    f.write(response)

soup = BeautifulSoup(response)
for link in soup.find_all("a"):
    text = link.get_text()
    if text == "Silvana_Prevails":
        print("go-go")