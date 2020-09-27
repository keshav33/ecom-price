import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=iPhone%2011'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

r = requests.get(url, headers = headers)
htmlcontent = r.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
productPrice = soup.find("div", class_="_1vC4OE _2rQ-NK").text
# productPrice = productPrice[3:]
productName = soup.find("div", class_="_3wU53n").text
productLink = soup.find("a", class_="_31qSD5").get("href")
productLink = "https://paytmmall.com" + productLink
print(productLink)
print(productName)
print(productPrice)
print("done")