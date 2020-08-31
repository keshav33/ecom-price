# import requests
# from bs4 import BeautifulSoup

# url = 'https://paytmmall.com/shop/search?q=iPhone%2011'

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

# r = requests.get(url, headers = headers)
# htmlcontent = r.content

# soup = BeautifulSoup(htmlcontent, 'html.parser')
# productPrice = soup.find("div", class_="_2bo3").text
# # productPrice = productPrice[3:]
# productName = soup.find("div", class_="UGUy").text
# productLink = soup.find("a", class_="_8vVO").get("href")
# productLink = "https://paytmmall.com" + productLink
# print(productLink)
# print(productName)
# print(productPrice)

def fun1():
    global a
    a = 10
    return a
def fun2():
    print(fun1())
fun2()