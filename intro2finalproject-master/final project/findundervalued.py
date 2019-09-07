import csv



def findundervaluedmarket(threshold):
    data = open("wow.csv","r")
    arr = data.readlines()
    gelist = []
    for idx,i in enumerate(arr[1:]):
        gelist.append(i.split(","))
    dealslist = []
    for idx,i in enumerate(gelist):
        if (int(i[8]) - int(i[9]) > threshold):
            dealslist.append(i)

    #dealstring = []
#    for i in dealslist:
    #    tempstring = ''
    #    for jdx,j in enumerate(i):
#        if (idx < (len(i)-1)):
    #            tempstring += str(j) + ','
    #        else:
    #            tempstring += str(j)
    #    dealstring.append(tempstring)

    #print(dealstring)
    #with open('capitalism' + str(threshold) + '.csv','w') as stremz:

    data.close()
    return(dealslist)

print(findundervaluedmarket(400000) )
