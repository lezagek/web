# импортируется библиотеки JINJA2 для работы с макросами
from jinja2 import  Environment, FileSystemLoader 

# читается информация из файла-шаблона в переменную html
# with open('3 theory ind_test_template.html','r', encoding ='utf-8-sig') as f_template:
    # html = f_template.read()

# создается объект-шаблон с помощью метода Template() на основе информации, 
# прочитанной из файла-шаблона
# template = Template(html)

env = Environment(loader=FileSystemLoader('.')) 
template = env.get_template('3 theory ind_test_template.html') 

# добавляем информацию (имя, группа, успеваемость) о студентах,
# которая хранится в списке 
students =[           
    {'name': "Алина",             
     'program': "Бизнес-информатика",             
     'subjects': ["Базы данных", "Программирование", "Эконометрика", "Статистика"],
     'gender': 'ж'           
    },           
    {'name': "Вадим",             
      'program': "Экономика",             
      'subjects': ["Информатика", "Теория игр", "Экономика", "Эконометрика", "Статистика"],
      'gender': 'м'            
    },           
    {'name': "Ксения",             
       'program': "Экономика",             
       'subjects' :["Информатика", "Теория игр", "Статистика"],
       'gender': 'ж'           
    }          
    ] 

# напишем функцию add_spaces(), которая будет после каждой буквы 
# строки вставлять пробел
def add_spaces(text):
    return " ".join(text)

# сделаем доступной эту функцию из шаблона: 
template.globals["add_spaces"] = add_spaces 

# напишем функцию right_dis(), которая получает количество дисциплин n 
# и возвращает слово «дисциплина» в верном падеже

def right_dis(n):
    n = int(n)
    if 10 < n < 20:
        return str(n) + " дисциплин"
    else:
        match n % 10:
            case 1:
                return str(n) + " дисциплина"
            case 2 | 3 | 4:
                return str(n) + " дисциплины"
            case _:
                return str(n) + " дисциплин"
            
template.globals["right_dis"] = right_dis

# с помощью метода render() генерируется html-код, при этом в качестве параметров
# метода указываются имена переменных, используемые в шаблоне, которым присваиваются 
# конкретные значения

# Для вывода дисциплин каждого студента можно передавать в шаблон не весь список со 
# студентами, а информацию об одном студенте

result_html = template.render(users=students[1]) 
# В переменной result_html хранится код, полученный из шаблона

# полученный html-код можно сохранить в файл (test.html), который затем открыть 
# в браузере

#создадим файл для HTML-страницы 
with open('3 ind_test.html', 'w', encoding ='utf-8-sig') as f:
    # выводим сгенерированную страницу в файл 
    print(result_html, file=f)