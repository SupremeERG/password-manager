import sqlite3, hashlib
import urllib.parse as encoder

con = sqlite3.connect('passwords.db')
cur = con.cursor()

def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS passwords (site text PRIMARY KEY, username text, password text, id text)''')

def insert(site,username,password,id): # consider using a class
    site = encoder.quote(site, safe='')
    username = encoder.quote(username, safe='')
    password = encoder.quote(password, safe='')
    id= encoder.quote(id, safe='')

    cur.execute(''' INSERT OR IGNORE INTO passwords VALUES ('{}', '{}', '{}', '{}')'''.format(site, username, password, id))# adds row if "SKU1234" doesnt already exist
    con.commit()

def get_passwd(id):
    cur.execute(''' SELECT * FROM passwords WHERE id='{}' '''.format(id))
    return cur.fetchone()
    #return password
#con.commit()

def view():
    amt = cur.execute(""" SELECT COUNT(*) FROM passwords""").fetchall()[0][0]
    if amt == 0:
        return print("No passwords found")
    
    for row in cur.execute(""" SELECT * FROM passwords"""):
         
        print(f"site: {encoder.unquote(row[0])}\nusername: {encoder.unquote(row[1])}\npassword: {encoder.unquote(row[2])}\nID: {encoder.unquote(row[3])}\n-----------")
        
def delete(id):
    cur.execute(''' DELETE FROM passwords WHERE id='{}' '''.format(id))