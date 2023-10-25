import sqlite3

# создаём базу данных и устанавливаем соединение с ней
con = sqlite3.connect("lib.sqlite")

# поменяла здесь name_genre на genre_name
# создаём таблицу genre, заносим в неё записи
# con.executescript('''
#     CREATE TABLE IF NOT EXISTS genre(
#     genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     genre_name VARCHAR(30)
#     );

#     INSERT INTO genre (genre_name)
#     VALUES
#     ('Роман'),
#     ('Приключения'),
#     ('Детектив'),
#     ('Лирика'),
#     ('Фантастика'),
#     ('Фэнтези');
# ''')


# # создаём таблицу publisher, заносим в неё записи
# con.executescript('''
#         CREATE TABLE IF NOT EXISTS publisher(
#         publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         publisher_name VARCHAR(30)
#         );

#         INSERT INTO publisher (publisher_name)
#         VALUES
#         ('ЭКСМО'),
#         ('ДРОФА'),
#         ('АСТ')
# ''')


# # здесь Детектив вместо Поэзия из примера
# # создаём таблицу book, заносим в неё записи
# con.executescript('''
#         CREATE TABLE IF NOT EXISTS book(
#         book_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title VARCHAR(30),
#         genre_id INTEGER,
#         publisher_id INTEGER,
#         year_publication INTEGER,
#         available_numbers INTEGER,
#         FOREIGN KEY (genre_id)
#             REFERENCES genre (genre_id),
#         FOREIGN KEY (publisher_id)
#             REFERENCES publisher (publisher_id)
#         );

#         INSERT INTO book (title, genre_id, publisher_id, year_publication, available_numbers)
#         VALUES
#         ('Мастер и Маргарита', '1', '2', '2014', '5'),
#         ('Таинственный остров', '2', '2', '2015', '10'),
#         ('Бородино', '3', '3', '2015', '12'),
#         ('Дубровский', '1', '2', '2020', '7'),
#         ('Вокруг света за 80 дней', '2', '2', '2019', '5'),
#         ('Убийства по алфавиту', '1', '1', '2017', '9'),
#         ('Затерянный мир', '2', '1', '2020', '3'),
#         ('Герой нашего времени', '1', '3', '2017', '2'),
#         ('Смерть поэта', '3', '1', '2020', '2'),
#         ('Поэмы', '3', '3', '2019', '5')
# ''')

# удаление всех таблиц
# con.execute("DROP TABLE  genre")
# con.execute("DROP TABLE  publisher")
# con.execute("DROP TABLE  book")

# сохраняем информацию в базе данных
con.commit()

# создаём объект-курсор
cursor = con.cursor()

# # проверка таблицы genre
# cursor.execute("SELECT * FROM genre")
# print(cursor.fetchall())

# # проверка таблицы publisher
# cursor.execute("SELECT * FROM publisher")
# print(cursor.fetchall())

# # проверка таблицы book
# cursor.execute("SELECT * FROM book")
# print(cursor.fetchall())

# запрос по трём таблицам
# cursor.execute('''SELECT title AS 'Название', genre_name AS 'Жанр', publisher_name AS 'Издат-во', year_publication AS 'Год', available_numbers AS 'Кол-во'
#                 FROM genre, publisher, book
#                 WHERE genre.genre_id = book.genre_id AND publisher.publisher_id = book.publisher_id
# ''')
# print(cursor.fetchall())

# книги, название которых содержит заданный текстовый фрагмент
# cursor.execute('''
#                 SELECT title
#                 FROM book
#                 WHERE title LIKE "%" || :p_text || "%"
#                 ''', {"p_text": "по"})

# print(cursor.fetchall())

# Вывести книги (указать их жанр), количество которых принадлежит интервалу от a до b, включая границы (границы интервала передать в качестве параметра)
cursor.execute('''
                SELECT genre_name
                FROM genre, book
                WHERE available_numbers >= :a AND available_numbers <= :b AND book.genre_id = genre.genre_id
                ''', {"a": "1", "b": "2"})

print(cursor.fetchall())

# Вывести книги (указать их издательство), название которой состоит из одного слова, и книга издана после заданного года (год передать в качестве параметра)
# надо ещё подумать
cursor.execute('''
                SELECT publisher_name
                FROM publisher, book
                WHERE title LIKE "^[А-Я]([а-я])+" AND year_publication > :year
                ''', {"year": "2017"})

print(cursor.fetchall())

# Вычислить, сколько экземпляров книг каждого жанра представлены в библиотеке. Учитывать только книги, изданные после заданного года (год передать в качестве параметра).
# надо ещё подумать
cursor.execute('''
                SELECT genre_name
                FROM genre, book
                WHERE year_publication > :year AND book.genre_id = genre.genre_id
                ''', {"year": "2010"})

print(cursor.fetchall())

import pandas as pd

# df = pd.read_sql('''
#                 SELECT
#                 title AS Название,
#                 publisher_id AS Издательство,
#                 genre_id AS Жанр,
#                 year_publication AS Год
#                 FROM book
#                 WHERE genre_id = :p_genre
#                 ''', con, params={"p_genre": 3})
# print(df)

# вывести только строку
# print(df.loc[1])

# вывести только столбец
# print(df["Название"])

# Количество строк и столбцов
# print("Количество строк:", df.shape[0])
# print("Количество столбцов:", df.shape[1])

# значение поля
# print(df.at[1,"Год"])

# название столбцов
# print(df.dtypes.index)

# Отобрать информацию о книгах, количество которых больше 3. Столбцы назвать Книга, Жанр, Издательство и Количество.
# Вывести отобранную информацию:
# - в виде таблицы;
# - только столбец Название;
# - 3-ю строку результата запроса;
# - количество строк и столбцов в результате запроса;
# - названия столбцов.

df = pd.read_sql('''
                SELECT
                title AS Книга,
                genre_id AS Жанр,
                publisher_id AS Издательство,
                available_numbers AS Количество
                FROM book
                WHERE available_numbers > :p_numbers
                ''', con, params={"p_numbers": 3})
print(df, '\n')
print(df["Книга"], '\n')
print(df.loc[3], '\n')
print("Количество строк:", df.shape[0])
print("Количество столбцов:", df.shape[1], '\n')
print(df.dtypes.index, '\n')

# f-строки

# genre_list = (2, 3)
# df = pd.read_sql(f'''
#                 SELECT
#                 title AS Название,
#                 publisher_id AS Издательство,
#                 genre_id AS Жанр,
#                 year_publication AS Год
#                 FROM book
#                 WHERE genre_id in {genre_list}
#                 ''', con)
# print(df, '\n')

# Создать кортеж, в который включить название двух издательств. Реализовать запрос, который выводит книги издательств, входящих в кортеж, изданных с 2016 по 2019 года, включая границы.
publisher_name = ('ЭКСМО', 'АСТ')
df = pd.read_sql(f'''
                SELECT
                title AS Название,
                book.publisher_id AS Издательство,
                genre_id AS Жанр,
                year_publication AS Год
                FROM book, publisher
                WHERE book.publisher_id = publisher.publisher_id AND year_publication BETWEEN 2016 AND 2019 AND publisher.publisher_name IN {publisher_name}
                ''', con)
print(df, '\n')

con.close()