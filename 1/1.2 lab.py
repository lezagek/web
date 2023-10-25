import sqlite3  

# создаем базу данных и устанавливаем соединение с ней 
con = sqlite3.connect("library.sqlite")  
# создаем курсор 
cursor = con.cursor()  
# выбираем и выводим записи из таблиц author, reader 
cursor.execute('''     
               SELECT          
                    title,         
                    publisher_name,         
                    year_publication     
               FROM book          
                    JOIN genre USING (genre_id)         
                    JOIN publisher USING (publisher_id)     
               WHERE genre_name = :p_genre AND year_publication > :p_year 
               ''',{"p_genre": "Детектив", "p_year": 2016})  

print(cursor.fetchall())  
# закрываем соединение с базой 
con.close() 