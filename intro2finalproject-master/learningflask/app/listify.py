import csv


def listifycsv(csvpath, title = False):
    data = open(csvpath,"r")
    arr = data.readlines()
    gelist = []
    if(title):
        gelist.append(arr[0].split(','))

    else:
        for idx,i in enumerate(arr[1:]):
            gelist.append(i.split(","))
    data.close()
    return (gelist)
