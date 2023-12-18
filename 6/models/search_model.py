import pandas as pd
import sqlite3

def get_count_genre(conn):
    return pd.read_sql('''
        SELECT genre_id, genre_name as Жанр, COUNT(book_id) AS Количество_книг
        FROM genre
        LEFT JOIN book USING(genre_id)
        GROUP BY genre.genre_id;
''', conn)


def get_count_author(conn):
    return pd.read_sql('''
        SELECT author.author_id, author_name as Автор, COUNT(book_author.book_id) AS Книги_автора
        FROM author
        LEFT JOIN book_author USING(author_id)
        GROUP BY author.author_id;
''', conn)


def get_count_publisher(conn):
    return pd.read_sql('''
        SELECT publisher.publisher_id, publisher_name as Издатель, COUNT(book.book_id) AS Книги_издателя
        FROM publisher
        LEFT JOIN book USING(publisher_id)
        GROUP BY publisher.publisher_id;
''', conn)


def get_book(conn):
    return pd.read_sql('''
    SELECT b.title AS Название, GROUP_CONCAT(a.author_name) AS Авторы, 
        g.genre_name AS Жанр, p.publisher_name AS Издательство, 
        b.year_publication AS Год_издания, b.available_numbers AS Количество, b.book_id AS ID_книги
    FROM book b
        JOIN book_author ba ON b.book_id = ba.book_id
        JOIN author a ON ba.author_id = a.author_id
        JOIN genre g ON b.genre_id = g.genre_id
        JOIN publisher p ON b.publisher_id = p.publisher_id
    GROUP BY b.book_id;
''', conn)


def get_filter_book(conn, genre, authors, publisher):
    if genre == []:
        genre = [1, 2, 3, 4, 5, 6]
   

    if authors == []:
        authors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
   

    if publisher == []:
        publisher = [1, 2, 3, 4, 5, 6, 7]

    query = '''
        SELECT b.title as Название, GROUP_CONCAT(a.author_name) AS Авторы,
        g.genre_name as Жанр, p.publisher_name as Издательство,
        b.year_publication as Год_публикации, b.available_numbers as Количество, b.book_id as Книга_id

        FROM book b
        JOIN book_author ba ON b.book_id = ba.book_id
        JOIN author a ON ba.author_id = a.author_id
        JOIN genre g ON b.genre_id = g.genre_id
        JOIN publisher p ON b.publisher_id = p.publisher_id

        WHERE g.genre_id IN ({})
          AND a.author_id IN ({})
          AND p.publisher_id IN ({})
        GROUP BY b.book_id;
    '''.format(','.join('?' * len(genre)), ','.join('?' * len(authors)), ','.join('?' * len(publisher)))

    params = tuple(genre + authors + publisher)
    return pd.read_sql(query, conn, params=params)
