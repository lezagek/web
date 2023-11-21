import pandas as pd

def get_genre(conn):     
    return pd.read_sql("SELECT * FROM genre", conn)

def get_book_genre(conn, genre_id, lower_limit, upper_limit):     
    return pd.read_sql(f'''
                       SELECT title AS Название,
                       genre_name AS Жанр,
                        (
                            SELECT GROUP_CONCAT(author_name, ', ')
                            FROM (book_author
                                    JOIN author USING (author_id)) AS b
                            WHERE a.book_id = b.book_id
                        ) AS Автор,
                        CASE
                            WHEN
                                book.available_numbers < {lower_limit}
                            THEN
                                'мало'
                            WHEN
                                book.available_numbers >= {lower_limit} AND book.available_numbers <= {upper_limit}
                            THEN
                                'достаточно'
                            ELSE
                                'много'
                        END AS Количество
                       FROM (book
                        JOIN genre USING (genre_id)
                        JOIN book_author USING(book_id)) AS a
                       WHERE genre_id = {genre_id}'''
                       , conn)