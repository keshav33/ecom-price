from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
from flask import Flask
from flask import request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
cors = CORS(app)

@app.route('/name', methods=['GET', 'POST'])
def getName():
    global data
    data = request.data
    data = str(data)
    return data

@app.route("/products")
def products():
    time.sleep(1)
    query = data.replace("'","")
    query = query[1:]
    query = query.replace(" ", "+")
    print(query)

    # For Flipkart
    try:
        url = 'https://www.flipkart.com/search?q='+query
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        r = requests.get(url, headers = headers)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        flipkartProductPrice = soup.find("div", class_="_1vC4OE _2rQ-NK").text
        flipkartProductPrice = flipkartProductPrice[1:].replace("₹", "-")
        flipkartProductPriceIndex = flipkartProductPrice.find("-")
        print(flipkartProductPriceIndex)
        if(flipkartProductPriceIndex > 0):
            flipkartProductPrice = flipkartProductPrice[:flipkartProductPriceIndex]
        flipkartProductName = soup.find("div", class_="_3wU53n").text
        flipkartProductLink = soup.find("a", class_="_31qSD5").get("href")
        flipkartProductLink = "https://www.flipkart.com" + flipkartProductLink
        flipkartProduct = {'companyName': 'Flipkart', 'productName': flipkartProductName, 'productPrice': flipkartProductPrice, 'productLink': flipkartProductLink}
    except:
        pass
    try:
        url = 'https://www.flipkart.com/search?q='+query
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        r = requests.get(url, headers = headers)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        flipkartProductPrice = soup.find("div", class_="_1vC4OE").text
        flipkartProductPrice = flipkartProductPrice[1:].replace("₹", "-")
        flipkartProductPriceIndex = flipkartProductPrice.find("-")
        print(flipkartProductPriceIndex)
        if(flipkartProductPriceIndex > 0):
            flipkartProductPrice = flipkartProductPrice[:flipkartProductPriceIndex]
        flipkartProductName = soup.find("a", class_="_2cLu-l").text
        flipkartProductLink = soup.find("a", class_="_2cLu-l").get("href")
        flipkartProductLink = "https://www.flipkart.com" + flipkartProductLink
        flipkartProduct = {'companyName': 'Flipkart', 'productName': flipkartProductName, 'productPrice': flipkartProductPrice, 'productLink': flipkartProductLink}
    except:
        flipkartProduct = {'companyName': 'Flipkart', 'productName': 'Null', 'productPrice': 'Null', 'productLink': 'Null'}

    # For Paytm
    try:
        query = query.replace("+","%20")
        url = 'https://paytmmall.com/shop/search?q='+query
        if(len(query)<1):
            url = 'https://paytmmall.com/'
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        r = requests.get(url, headers = headers)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        paytmProductPrice = soup.find("div", class_="_1kMS").text
        paytmProductName = soup.find("div", class_="UGUy").text
        paytmProductLink = soup.find("a", class_="_8vVO").get("href")
        paytmProductLink = "https://paytmmall.com" + paytmProductLink
        paytmProduct = {'companyName': 'Paytm', 'productName': paytmProductName, 'productPrice': paytmProductPrice, 'productLink': paytmProductLink}
    except:
        paytmProduct = {'companyName': 'Paytm', 'productName': 'Null', 'productPrice': 'Null', 'productLink': 'Null'}
    
    # For Amazon
    try:
        url = 'https://www.amazon.in/s?k='+query
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        r = requests.get(url, headers = headers)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        amazonProductPrice = soup.find("span", class_="a-price-whole").text
        try:
            amazonProductName = soup.find("span", class_="a-size-medium a-color-base a-text-normal").text
        except:
            amazonProductName = soup.find("span", class_="a-size-base-plus a-color-base a-text-normal").text
        amazonProductLink = soup.find("a", class_="a-link-normal a-text-normal").get("href")
        amazonProductLink = "https://www.amazon.in" + amazonProductLink
        companyName = 'Amazon'
        amazonProduct = {'companyName': companyName, 'productName': amazonProductName, 'productPrice': amazonProductPrice, 'productLink': amazonProductLink}
    except:
        amazonProduct = {'companyName': 'Amazon', 'productName': 'Null', 'productPrice': 'Null'}


    products = [amazonProduct, flipkartProduct, paytmProduct]
    return json.dumps(products)
    
app.run(debug=True)
