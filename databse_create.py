import sqlite3

conn = sqlite3.connect('chatdata2.db')
c=conn.cursor()
#c.execute("drop table parent_reply")
c.execute("CREATE TABLE IF NOT EXISTS parent_reply2(query TEXT , reply TEXT)")


