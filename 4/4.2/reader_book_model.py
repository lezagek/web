import pandas as pd

def get_reader(conn):     
    return pd.read_sql("SELECT * FROM reader", conn)

def get_book_reader(conn, reader_id):     
    return pd.read_sql(f'''
                       SELECT title AS Название,
                        (
                            SELECT GROUP_CONCAT(author_name, ', ')
                            FROM (book_author
                                    JOIN author USING (author_id)) AS b
                            WHERE a.book_id = b.book_id
                        ) AS Автор,
                        borrow_date AS Дата_выдачи,
                        return_date AS Дата_сдачи
                       FROM (book_reader
                        JOIN book USING(book_id)
                        JOIN book_author USING(book_id)) AS a
                       WHERE reader_id = {reader_id}'''
                       , conn)