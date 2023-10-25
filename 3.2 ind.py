from jinja2 import  Environment, FileSystemLoader

n = 5
a = 1
b = 5

h = (b - a) / (n - 1)

list = []
# for i in range(1, n + 1):
    

env = Environment(loader=FileSystemLoader('.')) 
template = env.get_template('3.2 ind template.html') 

result_html = template.render(list=list) 

with open('3.2 ind.html', 'w', encoding ='utf-8-sig') as f:
    print(result_html, file=f)