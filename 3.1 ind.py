import random
from jinja2 import  Environment, FileSystemLoader

n = 5
b = []
for i in range(1, n + 1):
    b.append(random.randint(0, 10))
name_list = "b"

env = Environment(loader=FileSystemLoader('.')) 
template = env.get_template('3.1 ind template.html') 

result_html = template.render(name=name_list, list=b) 

with open('3.1 ind.html', 'w', encoding ='utf-8-sig') as f:
    print(result_html, file=f)