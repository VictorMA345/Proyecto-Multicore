
from imports import *

#Recives a the string obteined from the web scrapping
#This function is specially for the games that have not discounts
#Returns the final price
def cleanFinalPrice(price):
    price = str(price)
    price = price.replace('<span class="psw-h3" data-qa="mfeCtaMain#offer0#finalPrice">',"")
    price = price.replace("</span>","")
    price = price.replace("US","")
    return price

#Recives a the string obteined from the web scrapping
#This function is used IF there is some discount in the game
#Returns the final price
def cleanOriginalPrice(originalPrice):
    originalPrice = str(originalPrice)
    originalPrice = originalPrice.replace('<span class="psw-h4 psw-c-secondary psw-text-strike-through" data-qa="mfeCtaMain#offer0#originalPrice">US',"")
    originalPrice = originalPrice.replace("</span>","")
    return originalPrice


#Main function that executes the web scrapping and return all the data cleaned
#Recives the URL of the PlayStation web of the game you want to stract the price.
def extraePrecioPlay(url):
    userAgent = {'User-agent':'Mozilla/5.0'}#This helps to enter the page without errors
    req = requests.get(url,headers = userAgent)
    soup = bs(req.text,'html.parser')
    
    finalPrice = soup.find_all('span',attrs = {"data-qa":"mfeCtaMain#offer0#finalPrice"})[0]#The actual price of the game
    finalPrice = cleanFinalPrice(finalPrice)

    originaPrice = None #In case there is some discount
    if(soup.find_all('span',attrs = {"data-qa":"mfeCtaMain#offer0#originalPrice"})):#If there is a discount
        originaPrice = soup.find_all('span',attrs = {"data-qa":"mfeCtaMain#offer0#originalPrice"})[0]#In case there are some discount
        originaPrice = cleanOriginalPrice(originaPrice)


    arrPrices = [originaPrice,finalPrice]

    return arrPrices
