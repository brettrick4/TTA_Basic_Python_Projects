import sqlite3
conn = sqlite3.connect('SQLite_Python.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('SQLite_Python.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('Hello.txt')"),
    cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('myMovie.mpg')"),
    cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('myPhoto.jpg')"),
    cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('myImage.png')"),
    cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('information.docx')"),
    cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('data.pdf')")
    
    conn.commit()
conn.close()


conn = sqlite3.connect('C:\sqlite\db\SQLite_Python.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileName FROM tbl_files WHERE col_fileName LIKE '%.txt%'")
    varfileName = cur.fetchall()
    for item in varfileName:
        msg = "File Names: {}".format(item[0])
        print(msg)







