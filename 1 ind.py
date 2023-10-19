import sqlite3  
import pandas as pd

# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("library.sqlite")

# Задание 1
df = pd.read_sql('''     
                 SELECT
                        title AS Название,
                        genre_name AS Жанр,
                        CASE
                            WHEN
                                book.available_numbers < '3'
                            THEN
                                'мало'
                            WHEN
                                book.available_numbers >= '3' AND book.available_numbers <= '5'
                            THEN
                                'достаточно'
                            ELSE
                                'много'
                        END AS Количество,         
                        publisher_name AS Издательство                       
                 FROM book          
                        JOIN genre USING (genre_id)
                        JOIN publisher USING (publisher_id)
                  WHERE title NOT LIKE '% %'
                 ''', con)

print('\n Задание 1 \n', df) 

# Задание 2
df = pd.read_sql('''     
                 SELECT          
                        genre_name AS Жанр,         
                        IFNULL(SUM(available_numbers), '-') AS Количество_экземпляров
                 FROM genre          
                        JOIN book USING (genre_id)
                 GROUP BY genre_name
                 ORDER BY Количество_экземпляров DESC, Жанр ASC
                 ''', con)

print('\n Задание 2 \n', df) 

# Задание 3
df = pd.read_sql('''
                 SELECT title AS Название,
                 (
                     SELECT GROUP_CONCAT(author_name, ', ')
                     FROM (book_author
                            JOIN author USING (author_id)) AS b
                     WHERE a.book_id = b.book_id
                 ) AS Автор

                 FROM (book_reader
                     JOIN book USING (book_id)
                     JOIN book_author USING (book_id)) AS a
                 WHERE reader_id = (
                     SELECT reader_id
                     FROM book_reader
                     GROUP BY reader_id
                     HAVING COUNT(reader_id) = (
                            SELECT MAX(count_reader)
                            FROM
                                   (
                                   SELECT
                                          reader_id, COUNT(reader_id) AS count_reader
                                   FROM 
                                          book_reader
                                   GROUP BY reader_id
                                   ) query_in
                     )
                 )
                 GROUP BY book_id
                 ''', con)

print('\n Задание 3 \n', df)

# Задание 4
con.execute('''     
                 CREATE TABLE IF NOT EXISTS rating AS
                 SELECT reader_id AS Читатель,
                 SUM(
                     CASE
                            WHEN
                                   (julianday(return_date) - julianday(borrow_date)) < 14.0
                            THEN
                                   5
                            WHEN
                                   (julianday(return_date) - julianday(borrow_date)) >= 14.0 AND (julianday(return_date) - julianday(borrow_date)) <= 30.0
                            THEN
                                   2
                            WHEN
                                   (julianday(return_date) - julianday(borrow_date)) > 30.0
                            THEN
                                   -2
                            WHEN
                                   return_date IS NULL
                            THEN
                                   1
                            ELSE
                                   0
                     END           
                 ) AS Баллы
                 FROM book_reader
                 GROUP BY reader_id;
                 ''')

# con.execute("DROP TABLE rating")

con.commit()  
df = pd.read_sql('''     
                 SELECT *
                 FROM rating
                 ''', con)

print('\n Задание 4 \n', df) 

# Задание 5
df = pd.read_sql('''
              WITH get_reader_book(book_id, pop_book)
              AS (
                     SELECT book_id, COUNT(book_id) AS pop_book
                     FROM book_reader
                            JOIN book USING (book_id)
                     GROUP BY book_id
              ),
                 
              get_genre(genre_id, genre_num)
              AS (
                 SELECT genre_id, COUNT(genre_id) AS genre_num
                     FROM genre
                            JOIN book USING (genre_id)
                            JOIN book_reader USING (book_id)
                     GROUP BY genre_id
              ),
              
              get_book(Автор, title, available_numbers, genre_id, genre_num, pop_book) 
              AS (
                 SELECT
                 (
                     SELECT GROUP_CONCAT(author_name, ', ')
                     FROM (book_author
                            JOIN author USING (author_id)) AS b
                     WHERE a.book_id = b.book_id
                 ) AS Автор,
                 title, available_numbers, book.genre_id, genre_num, pop_book
                 FROM (author
                     JOIN book_author USING (author_id)
                     JOIN book USING (book_id)
                     JOIN get_reader_book USING (book_id)
                     JOIN get_genre USING (genre_id)) AS a
                 GROUP BY Автор, title
              )
              
              SELECT DISTINCT
                 Автор,
                 FIRST_VALUE(title) OVER win_book AS Книга
              FROM get_book
              WINDOW win_book
              AS(
                 PARTITION BY Автор
                 ORDER BY pop_book DESC, genre_num DESC, available_numbers DESC
              )
              ORDER BY Автор, Книга
                 ''', con)


print('\n Задание 5 \n', df)

# закрываем соединение с базой 
con.close() 