from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime
import pandas

excel_data_df = pandas.read_excel('wine.xlsx')
wine_data = excel_data_df.to_dict('records')
print(wine_data)


event1 = datetime.datetime.now()
event2 = datetime.datetime(year=1920, month=1, day=1)
age = event1.year - event2.year

age_declensions = (age % 100)

if age_declensions >=11 and age_declensions <=19:
    age_declensions = 'лет'
else: 
    age_declensions = (age_declensions % 10) 
    if age_declensions == 1:
        age_declensions ='год'
    elif age_declensions >= 2 and age_declensions <=4:
        age_declensions ='года'
    else:
        age_declensions ='лет'

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_age = template.render(
    winery_text='мы уже {} {} с вами'.format(age, age_declensions),
    
)

rendered_wine = template.render(wine_data=wine_data)

with open('index.html', 'w', encoding="utf-8") as file:
    file.write(rendered_wine)

with open('index.html', 'w', encoding="utf-8") as file:
    file.write(rendered_age)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()