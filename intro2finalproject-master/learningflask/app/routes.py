from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, UnderValuedForm
from listify import listifycsv
import picscraper
import findundervaluedsingleitem
import undervaluedstack
import pygal







#@app.route('/datapresent', methods=['GET', 'POST'])
#def datapresent():
#    data = []
#    you = listifycsv('wow.csv', True)
#    deals  = findundervalued()
#    for i in range(len(deals)):
#        data.append({})
#    counter = 0
#    counter2 = 0
#    while (counter < len(deals)):
#        data[counter] =

#@app.route('/undervalued')
#def undervaluedgraph():
#    form = UnderValuedForm()
#    if form.validate_on_submit():

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.route('/index')
@app.route('/undervalued', methods=['GET', 'POST'])
def undervalued():
    form = UnderValuedForm()

    if form.validate_on_submit():
        print('hi')
        line_out_data = []

        titleholder = listifycsv('wow.csv', True)[0]
        dataholder = eval(form.SearchType.data).findundervaluedmarket(int(form.ListDepth.data))

        for i in dataholder:
            line_chart = pygal.Bar()
            line_chart.title = i[1] + ', ' + i[3] + ', ' + i[4] + ', ' + str(i[0])
            line_chart.x_labels = ['Gold']
            #line_chart.x_labels = titleholder[0][7:9]
            line_chart.add(titleholder[7],  i[7] / 10000)
            line_chart.add(titleholder[8],    i[8] / 10000)
            line_chart_data = line_chart.render_data_uri()
            line_out_data.append(line_chart_data)
        return render_template("undervalued.html",  line_out_data = line_out_data, form=form, title = "Undervalued single item")
    flash_errors(form)
    return render_template('undervalued.html', title='tets', form=form, )
