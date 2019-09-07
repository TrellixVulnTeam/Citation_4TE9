from listify import listifycsv

def templatefrombase(csvhere, templatename):
    data = open("learningflask/app/templates/" + templatename + ".html", "w")
    conditionalnames = listifycsv('wow.csv', True)
    data.write('{% extends "base.html" %}\n\n' + '{% block content %} \n')
    data.write('{% for title in data %}')
    data.write('<div>\n <p>')

    for i in conditionalnames[0]:
        print(i)
        data.write(i + ' : {{ title.' + i + '}} ')

    data.write('</p>\n </div>\n')
    data.write('{% endfor %}\n')
    data.write('{% endblock %}')






    data.close()
    return(5)



print(templatefrombase('wow.csv','datapresent'))
