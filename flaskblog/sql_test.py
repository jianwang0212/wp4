import sqlite3


############# Original Database ######################
conn = sqlite3.connect('29_dec_site.db')

c = conn.cursor()

# c.execute(INSERT INTO "")

c.execute("SELECT * FROM category")
import_table = c.fetchall()
conn.commit()
conn.close

############# Target Database ######################
conn = sqlite3.connect('site.db')

c = conn.cursor()


def remove_table():
    with conn:
        c.execute("DELETE FROM category")


remove_table()  # remove all existing category
# print()
for element in import_table:
    c.execute("INSERT INTO category VALUES (?,?,?)",
              element + (None,))

conn.commit()
conn.close
