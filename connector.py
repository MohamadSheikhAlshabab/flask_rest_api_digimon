import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234!@#QWE123qwe",
  database="digimons_db"
)
print(mydb)
mycursor = mydb.cursor()
print(mycursor)

# CREATE DATABASE 
def create_db():
    try:
        mycursor.execute("CREATE DATABASE if not exists digimons_db")
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)
    except Exception as err:
        print(err)


# CREATE TABLE 
def create_table():
    try:
        mycursor.execute("CREATE TABLE  if not exists digimons (name VARCHAR(255), img VARCHAR(255), level VARCHAR(255))")
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
            print(x)
    except Exception as err:
        print(err)

# INSERT INTO TABLE 
def insert_to_table(name,img,level):
    try:
        sql = "INSERT INTO digimons (name, img, level) VALUES (%s, %s, %s)"
        val = (name,img,level)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Exception as err:
        sql = "REPLACE INTO digimons (name, img, level) VALUES (%s, %s, %s)"
        val = (name,img,level)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        print(err)

# SELECT TABLE
def select_table():
    try:
        mycursor.execute("SELECT * FROM digimons")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    except Exception as err:
        print(err)


# SELECT name from TABLE
def select_names():
    try:
        mycursor.execute("SELECT name FROM digimons")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    except Exception as err:
        print(err)

# SELECT img from TABLE
def select_imgs():
    try:
        mycursor.execute("SELECT img FROM digimons")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    except Exception as err:
        print(err)

# SELECT level from TABLE
def select_levels():
    try:
        mycursor.execute("SELECT level FROM digimons")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    except Exception as err:
        print(err)

# DELETE by level from TABLE
def delete_by_level(level):
    try:
        sql = "DELETE FROM digimons WHERE level = '%s'"
        val = level
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    except Exception as err:
        print(err)

# DELETE by name from TABLE
def delete_by_name(name):
    try:
        sql = "DELETE FROM digimons WHERE name = '%s'"
        val = name
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    except Exception as err:
        print(err)

# DELETE by img from TABLE
def delete_by_img(img):
    try:
        sql = "DELETE FROM digimons WHERE img = '%s'"
        val = img
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    except Exception as err:
        print(err)

# DELETE TABLE
def drop_table():
    try:
        sql = "DROP TABLE IF EXISTS digimons"
        mycursor.execute(sql)
    except Exception as err:
        print(err)

# Update by level from Table
def update_level(level):
    try:
        sql = "UPDATE digimons SET level = '%s' WHERE level = '%s'"
        val = level
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    except Exception as err:
        print(err)

# Update by name from Table
def update_name(name):
    try:
        sql = "UPDATE digimons SET name = '%s' WHERE name = '%s'"
        val = name
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    except Exception as err:
        print(err)

# Update by img from Table
def update_img(img):
    try:
        sql = "UPDATE digimons SET img = '%s' WHERE img = '%s'"
        val = img
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    except Exception as err:
        print(err)