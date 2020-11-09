
from imports import *


#Recives the string stracted by the scrapping and cleans it until it has only the information we need.
#Returns an array that contains the category and the amount of hours need to complete the game in the corresponding category.
def separaInfo(stringInfo):
    #Cleaning the string
    stringInfo = str(stringInfo)
    stringInfo = stringInfo.replace('<li class="short time_100">',"")
    stringInfo = stringInfo.replace("<h5>","")
    stringInfo = stringInfo.replace("</h5>"," ")
    stringInfo = stringInfo.replace("<div>","")
    stringInfo = stringInfo.replace("</div>","")
    stringInfo = stringInfo.replace("</li>","")

    splited = stringInfo.split("\n")#We need to split it to return the category and the amount of hours separated into a string

    title = splited[1]
    hours = splited[2]

    info = [title,hours]
    return info

#Returns an array that have all the information we need.
#Recives the array extracted by the web scraping.
def creaArrInfo(arrElements):
    #We separete the given information into their different categories used
    mainStory = separaInfo(arrElements[0])
    mainPExtras = separaInfo(arrElements[1])
    completionist = separaInfo(arrElements[2])
    speedRun = separaInfo(arrElements[3])

    arrInfo = [mainStory,mainPExtras,completionist,speedRun]
    return arrInfo

#Do the web scrapping and return the information in an array
def extraeTiempoPasar(url):
    userAgent = {'User-agent':'Mozilla/5.0'}#This helps to enter the page without errors
    req = requests.get(url,headers = userAgent)
    soup = bs(req.text,'html.parser')
    times = soup.find_all('li',attrs = {"class":"short time_100"})
    
    arrInfo = creaArrInfo(times)

    return arrInfo



