# импортируем необходимые модули 
from jinja2 import FileSystemLoader, Environment
import sqlite3 
from library_model import get_publisher,  get_genre, get_reader, get_author, get_book_author, get_book, get_book_reader

# устанавливаем соединение с базой данных (базу данных взять из ЛР 1) 
conn = sqlite3.connect("library.sqlite")  

# выбираем записи из таблиц
df_publisher = get_publisher(conn)
df_genre = get_genre(conn)
df_reader = get_reader(conn)
df_author = get_author(conn)
df_book_author = get_book_author(conn)
df_book = get_book(conn)
df_book_reader = get_book_reader(conn)

# закрываем соединение с базой 
conn.close()  

env = Environment(loader=FileSystemLoader('.')) 
template = env.get_template('library_templ.html') 

# генерируем результат на основе шаблона 
result_html = template.render(tables = {
    "publisher": df_publisher,
    "genre": df_genre,
    "reader": df_reader,
    "author": df_author,
    "book_author": df_book_author,
    "book": df_book,
    "book_reader": df_book_reader
})  
    
# выводим сгенерированную страницу в файл 
with open('library.html', 'w', encoding ='utf-8-sig') as f:
    print(result_html, file=f)