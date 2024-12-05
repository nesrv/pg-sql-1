import sqlite3;
# создаем подключение
con = sqlite3.connect("books.db")
print (123) # получаем курсор
cursor = con.cursor()
