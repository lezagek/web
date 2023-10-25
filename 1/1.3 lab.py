import sqlite3  
import pandas as pd 

# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("library.sqlite")
# выбираем и выводим записи из таблиц author, reader 
df = pd.read_sql('''     
                 SELECT          
                        title AS Название,         
                        publisher_name AS Издательство,         
                        year_publication AS Год     
                 FROM book          
                        JOIN genre USING (genre_id)         
                        JOIN publisher USING (publisher_id)     
                 WHERE genre_name = :p_genre AND year_publication > :p_year 
                 ''', con, params={"p_genre": "Роман", "p_year": 2016})  

print(df)  
# закрываем соединение с базой 
con.close() 