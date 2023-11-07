# from collections import Counter
# import nltk
from nltk.tokenize import word_tokenize
# from SQL import SQL
import sqlite3
# class Counter:


# nltk.download()
    # def count(self):
CONNECTION = sqlite3.connect('diplom.db')
cursor = CONNECTION.cursor()
cursor1 = CONNECTION.cursor()
cursor.execute("SELECT HEADER, TRANSCRIPT FROM GD_TRANSCRIPTS")


for result in cursor:
    words = {'демократия': 0, 'выборы': 0, 'парламент': 0, 'суд': 0, 'референдум': 0,
                 'гражданское общество': 0}
    # c = 0
    date = result[0]
    text = result[1]
    transcript = word_tokenize(text.lower())

    for word in transcript:
        if 'демократ' in word and 'либерально-демократ' not in word:
            words['демократия'] += 1
        elif 'выборы' in word or 'выборн' in word:
            words['выборы'] += 1
        elif 'парламентарн' in word or 'парламентск' in word:
            words['парламент'] += 1
        elif 'судебн' in word:
            words['суд'] += 1
        elif 'референдум' in word:
            words['референдум'] += 1
        elif 'гражданско' in word:
            words['гражданское общество'] += 1

    # if c:
    print(date, 'inserted')
    cursor1.execute(f"INSERT INTO GD_COUNT (GD_DATE, DEMOCRACY, ELECTIONS, PARLAMENT, COURT , REFERENDUM, SOCIETY) VALUES ('{date}', {words['демократия']}, {words['выборы']}, {words['парламент']}, {words['суд']}, {words['референдум']}, {words['гражданское общество']})")
    CONNECTION.commit()
    # else:
    #     print(date, 'nope')

CONNECTION.close()
