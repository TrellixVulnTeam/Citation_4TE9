from bs4 import BeautifulSoup
#import csv
from selenium import webdriver
#from selenium.webdriver.chrome.chrome.chrome_binary import ChromeBinary

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ("")

def itemcode(pgetgt):
    return(find_between(pgetgt, "item=", "/"))

def itemnumtoitempic(itemnum):
    pagetarget = "http://www.wowhead.com/item=" + str(itemnum) +"/"
    driver = webdriver.Chrome('C:/Users/Jesster/Documents/GitHub/intro2finalproject/learningflask/chromedriver.exe')
    driver.get(pagetarget)
    html = driver.page_source
    soup = BeautifulSoup (html, "html5lib")
    picdiv = (soup.find(id = ("ic" + itemcode(pagetarget))))
    narrowing = (picdiv.find('ins'))
    narrowing.get('style')
    imgurl = "http://" + find_between((narrowing.get('style')), '//', '"')
    driver.quit()
    return(imgurl)


print(itemnumtoitempic(4536))
