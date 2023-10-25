import math
from jinja2 import  Environment, FileSystemLoader

n = 5
a = 1
b = 5

h = (b - a) / (n - 1)
num = a

list = []
for i in range(n):
    list.append({})
    list[i]["x"] = num
    list[i]["f(x)"] = math.sin(num)
    list[i]["y(x)"] = math.cos(num)
    num +=h

first_row = 1
last_row = 5

env = Environment(loader=FileSystemLoader('.')) 
template = env.get_template('3.2 ind template.html') 

result_html = template.render(list=list, first_row=first_row, last_row=last_row) 

with open('3.2 ind.html', 'w', encoding ='utf-8-sig') as f:
    print(result_html, file=f)