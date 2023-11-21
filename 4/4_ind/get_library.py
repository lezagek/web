# импортируем необходимые модули 
from jinja2 import FileSystemLoader, Environment
import sqlite3 
from book_genre_model import get_genre, get_book_genre

# задаем id жанра, для которого формируем страницу 
genre_id = 3

# задаем нижнюю границу для "мало" и верхнюю для "много"
lower_limit = 3
upper_limit = 5

# устанавливаем соединение с базой данных (базу данных взять из ЛР 1) 
conn = sqlite3.connect("library.sqlite")  

# выбираем записи  о том, какие книги есть в библиотеке с жанром genre_id 
# столбцы назвать Название, Жанр, Авторы, Количество
df_book_genre = get_book_genre(conn, genre_id, lower_limit, upper_limit)


# выбираем записи из таблицы genre для формирования поля со списком 
df_genre = get_genre(conn)

# закрываем соединение с базой 
conn.close()  

env = Environment(loader=FileSystemLoader('.')) 
template = env.get_template('book_genre_templ.html') 

# генерируем результат на основе шаблона 
result_html = template.render(                               
    genre_id = genre_id,                               
    combo_box = df_genre,                               
    book_genre = df_book_genre,                               
    len = len,
    lower_limit = lower_limit,
    upper_limit = upper_limit
)
    
# выводим сгенерированную страницу в файл 
with open('book_genre.html', 'w', encoding ='utf-8-sig') as f:
    print(result_html, file=f)