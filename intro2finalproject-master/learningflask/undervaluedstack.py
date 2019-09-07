import csv
from listify import listifycsv


def getundervalue(incoming):
    if (float(incoming[8]) == 0.0):
        return(0)
    else:
        return((int(incoming[7])- int(incoming[8])) * int(incoming[9]))


def findundervaluedmarket(howmany = 10):
    gelist = listifycsv("wow.csv")
    dealslist = (sorted(gelist, key=getundervalue, reverse=True)[:howmany])
    for idx, i in enumerate(dealslist):
        for jdx,j in enumerate(i):
            try:
                dealslist[idx][jdx] = float(j)
            except ValueError:
                nothing = 0


    return(dealslist)
    #with open('capitalism' + str(threshold) + '.csv','w') as stremz:

    #data.close()


#print(findundervaluedmarket())


print('hello')
