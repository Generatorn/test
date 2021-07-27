import requests
from bs4 import BeautifulSoup

#link = "https://codeforces.com/profile/Silvana_Prevails"
#response = requests.get(link).text
#with open("out.html", "w", encoding="utf8") as f:
#    f.write(response)

#soup = BeautifulSoup(response)
#for link in soup.find_all("a"):
#    text = link.get_text()
#    if text == "Silvana_Prevails":
#        print("go-go")
print("hello")
for i in range(11):
    print(i + 1)
j = 12
print(j)


class Rectangle:
    default_color = "green"

    def __init__(self, width, height):
        self.width = width
        self.height = height
