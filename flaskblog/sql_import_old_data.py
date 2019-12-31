import sqlite3


############# Original Database ######################
conn = sqlite3.connect('29_dec_site.db')

c = conn.cursor()

c.execute("SELECT * FROM category") # select all columns from the table "category"
# c.execute("SELECT * FROM category WHERE id = 1")
# c.execute("SELECT * FROM category WHERE id =:id", {'id': 1})

# c.exeute("INSERT INTO category VALUES (1,'what','date')")
# c.exeute("INSERT INTO category VALUES (:id, :category, :date)", {'id':1, 'category':'high service', 'date':'1,1'})

# c.execute("""UPDATE category SET category = :category
#     WHERE id=:id,
#     {'category':'high service', 'id':1}
#     """)
# c.execute("DELETE from category WHERE id =:id", {'id':1})

import_table = c.fetchall()
print(import_table) # a list of tuple
conn.commit()
conn.close

############# Target Database ######################
conn = sqlite3.connect('site.db')

c = conn.cursor()


def remove_table(): # delete all contents in a table
    with conn:
        c.execute("DELETE FROM category")


remove_table()  # remove all existing category
# print()
for element in import_table:
    c.execute("INSERT INTO category VALUES (?,?,?)",
              element + (None,)) # insert values into table

conn.commit()
conn.close
