from bs4 import BeautifulSoup
import csv


filemagic = open("final project\wowdatanonscraped.csv","r")
fileread = filemagic.readlines()
test  = 10
while (test > 0):
    print(fileread[test])
    test -= 1
filemagic.close()
