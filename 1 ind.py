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

# df = pd.read_sql('''
#                  SELECT
#                             reader_id, COUNT(reader_id)
#                             FROM book_reader
#                             GROUP BY reader_id
#                             ORDER BY COUNT(reader_id) DESC
#                             LIMIT 1
                 
#                  ''', con)

# print('\n Задание 3 \n', df)

# df = pd.read_sql('''
#                  SELECT
#                      title, author_id
#                  FROM book_reader
#                      JOIN book USING (book_id)
#                      JOIN book_author USING (book_id)
                 
#                  WHERE reader_id = (
#                             SELECT
#                                    reader_id
#                             FROM book_reader
#                             GROUP BY reader_id
#                             ORDER BY COUNT(reader_id) DESC
#                             LIMIT 1
#                      )
                     

                 
#                  ''', con)

# print('\n Задание 3 \n', df)

# df = pd.read_sql('''
#                  SELECT
#                      title AS Название, 
#                      (
#                             SELECT GROUP_CONCAT(author_name, ', ')
#                             FROM (book_author
#                                    JOIN author USING (author_id)) AS b
#                             WHERE a.book_id = b.book_id
#                      ) AS Автор
#                  FROM (book_reader
#                      JOIN book USING (book_id)
#                      JOIN book_author USING (book_id)) AS a
                 
#                  WHERE reader_id = (
#                             SELECT
#                                    reader_id
#                             FROM book_reader
#                             GROUP BY reader_id
#                             ORDER BY COUNT(reader_id) DESC
#                             LIMIT 1
#                      )
#                  GROUP BY title
#                  ''', con)

# print('\n Задание 3 \n', df)

# df = pd.read_sql('''
#                  SELECT reader_id
#                  FROM book_reader
#                  GROUP BY reader_id
#                  HAVING COUNT(reader_id) = (
#                      SELECT MAX(count_reader)
#                      FROM
#                             (
#                             SELECT
#                                    reader_id, COUNT(reader_id) AS count_reader
#                             FROM 
#                                    book_reader
#                             GROUP BY reader_id
#                             ) query_in
#                  )
                 

                 
#                  ''', con)

# print('\n Задание 3 \n', df)

# df = pd.read_sql('''
#                  SELECT title, reader_id
#                  FROM
#                      book INNER JOIN book_reader
#                      on book.book_id = book_reader.book_id
                 
#                  ''', con)

# print('\n Задание 3 \n', df)

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

# df = pd.read_sql('''
#                  SELECT reader_id
#                  FROM
#                      book_reader
#                  GROUP BY reader_id
#                  HAVING COUNT(reader_id) =
#                      (
#                             SELECT MAX(count_reader)
#                             FROM
#                                    (
#                                    SELECT
#                                           reader_id, COUNT(reader_id) AS count_reader
#                                    FROM 
#                                           book_reader
#                                    GROUP BY reader_id
#                                    ) query_in
#                      )
#                  ''', con)

# print('\n Задание 3 \n', df)

# df = pd.read_sql('''
#                  SELECT title
#                  FROM
#                      book INNER JOIN book_reader
#                      on book.book_id = book_reader.book_id
#                  GROUP BY reader_id
#                  HAVING COUNT(reader_id) =
#                      (
#                             SELECT MAX(count_reader)
#                             FROM
#                                    (
#                                    SELECT
#                                           reader_id, COUNT(reader_id) AS count_reader
#                                    FROM 
#                                           book_reader
#                                    GROUP BY reader_id
#                                    ) query_in
#                      )
#                  ''', con)

# print('\n Задание 3 \n', df)

# df = pd.read_sql('''
#                  SELECT
#                      title,
#                      (
#                             SELECT GROUP_CONCAT(author_name, ',')
#                             FROM (book_reader
#                                           JOIN book USING (book_id)
#                                           JOIN book_author USING (book_id)
#                                           JOIN author USING (author_id)
#                                    ) AS b 
#                             WHERE a.title = b.title
#                             GROUP BY title
#                      ) AS Автор
#                      FROM (book_reader
#                             JOIN book USING (book_id)
#                             JOIN book_author USING (book_id)
#                             JOIN author USING (author_id)
#                             ) AS a
#                      WHERE reader_id = (
#                             SELECT
#                                    reader_id
#                             FROM book_reader
#                             GROUP BY reader_id
#                             ORDER BY COUNT(reader_id) DESC
#                             LIMIT 1
#                      )
#                      GROUP BY title
                 
#                  ''', con)

# print('\n Задание 3 \n', df)

# df = pd.read_sql('''
#                  SELECT 
#                      title AS Название,
#                      (
#                             SELECT
#                                    GROUP_CONCAT(author_name, ',')
#                             FROM (
#                                    SELECT DISTINCT a.title, a.author_name
#                                    FROM (book_reader
#                                           JOIN book USING (book_id)
#                                           JOIN book_author USING (book_id)
#                                           JOIN author USING (author_id)
#                                    ) AS a
#                             ) AS sub
#                             WHERE main.title = sub.title
#                             GROUP BY sub.title
#                      ) AS Автор
#                  FROM (
#                      SELECT DISTINCT b.title
#                      FROM (book_reader
#                             JOIN book USING (book_id)
#                             JOIN book_author USING (book_id)
#                             JOIN author USING (author_id)
#                      ) AS b
#                  ) AS main
                 
                 
                 
#                  ''', con)

# print('\n Задание 3 \n', df)

# для проверки количества дней
# df = pd.read_sql('''
#                  SELECT 
#                      reader_id AS Читатель,
#                      (julianday(return_date) - julianday(borrow_date)) AS Дни
#                  FROM book_reader
#                  ''', con)

# print(df, '\n')

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
# df = pd.read_sql('''
#                  SELECT DISTINCT
#                      Название
#                      Автор,
#                      MAX(Макс)
#                      OVER (PARTITION BY Автор) AS Макс
#                  FROM
#                  (
#                      SELECT
#                             title AS Название,
#                             (
#                                    SELECT GROUP_CONCAT(author_name, ', ')
#                                    FROM (
#                                           book_author
#                                           JOIN author USING (author_id)
#                                    ) AS b
#                                    WHERE a.book_id = b.book_id
#                             ) AS Автор,
#                             COUNT(*) AS Макс
#                      FROM
#                      (
#                             book_author
#                             JOIN author USING (author_id)
#                             JOIN book USING (book_id)
#                             JOIN book_reader USING (book_id)
#                      ) AS a


#                      GROUP BY
#                             book.title,
#                             Автор
#                  ) AS sub

#                  ORDER BY
#                      Автор ASC,
#                      Название ASC
                 
#                  ''', con)

# print('\n Задание 5 \n', df)

df = pd.read_sql('''
              WITH popular_books AS (
              SELECT 
                     b.title AS Название,
                     GROUP_CONCAT(DISTINCT a.author_name) AS Авторы,
                     ROW_NUMBER() OVER (
                     PARTITION BY a.author_name 
                     ORDER BY 
                            COUNT(*) DESC, 
                            MAX(g.genre_count) DESC, 
                            b.available_numbers DESC
                     ) AS rn
              FROM 
                     book b
                     JOIN book_author ba ON b.book_id = ba.book_id
                     JOIN author a ON ba.author_id = a.author_id
                     JOIN (
                            SELECT 
                                   br.book_id,
                                   COUNT(*) AS genre_count
                            FROM 
                                   book_reader br
                                   JOIN book b1 ON br.book_id = b1.book_id
                            GROUP BY 
                                   br.book_id
                     ) g ON b.book_id = g.book_id
                     JOIN book_reader br ON b.book_id = br.book_id
              GROUP BY 
                     ba.book_id, b.title
              ),
              genre_counts AS (
              SELECT 
                     genre_id,
                     COUNT(*) AS genre_count
              FROM 
                     book_reader br
                     JOIN book b ON br.book_id = b.book_id
              GROUP BY 
                     genre_id
              )
              SELECT 
              Название,
              Авторы AS Автор
              FROM 
              (
                     SELECT 
                     p.Название,
                     p.Авторы,
                     ROW_NUMBER() OVER (
                            PARTITION BY p.Авторы 
                            ORDER BY 
                            p.rn
                     ) AS row_num
                     FROM 
                     popular_books p
              ) ranked_books
              WHERE 
              row_num = 1
              ORDER BY 
              Автор ASC, Название ASC;          
                 ''', con)

print('\n Задание 5 \n', df)

# df = pd.read_sql('''
#               WITH popular_books AS (
#               )     
#                  ''', con)

# print('\n Задание 5 \n', df)

# df = pd.read_sql('''
#                  SELECT DISTINCT
#                      title AS Название,
#                      Автор,
#                      MAX(row_num)
#                      OVER (PARTITION BY Автор) AS Макс
#                  FROM
#                  (
#                      SELECT
#                             book.title,
#                             (
#                                    SELECT GROUP_CONCAT(author_name, ', ')
#                                    FROM
#                                           book_author
#                                           JOIN author USING (author_id)
#                                           WHERE book.book_id = book_author.book_id
#                             ) AS Автор,
#                             ROW_NUMBER()
#                             OVER (
#                                    PARTITION BY book.title, Автор 
#                                    ORDER BY book.book_id
#                             ) AS row_num
#                      FROM
#                             book
#                             JOIN book_author USING (book_id)
#                             JOIN author USING (author_id)

#                  ) AS sub

#                  ORDER BY
#                      Автор ASC,
#                      Название ASC
                 
#                  ''', con)

# print('\n Задание 5 \n', df)

# df = pd.read_sql('''
#                  SELECT DISTINCT
#                      title AS Название,
#                      (
#                             SELECT GROUP_CONCAT(author_name, ', ')
#                             FROM (book_author
#                                    JOIN author USING (author_id)
#                                    )AS b
#                             WHERE a.book_id = b.book_id
#                      ) AS Автор,
                     
#                      MAX(
#                             COUNT(*)
#                             OVER (
#                                    PARTITION BY title
#                             )
#                      )
#                      OVER (
#                             PARTITION BY Автор
#                      ) AS Макс
                     
#                  FROM
#                      (book_author
#                      JOIN author USING (author_id)
#                      JOIN book USING (book_id)
#                      JOIN book_reader USING (book_id)
#                      )AS a
#                  ORDER BY
#                      Автор ASC,
#                      Название ASC
                 
#                  ''', con)

# print('\n Задание 5 \n', df)

# закрываем соединение с базой 
con.close() 