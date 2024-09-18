from sqlite3 import connect


class Database:

    db = None

    @staticmethod
    def connecDataBase():
        Database.db = connect("number.db")

        cursor = Database.db.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, email text NOT NULL, password text NOT NULL )')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS fact_table(id integer PRIMARY KEY, email text NOT NULL, fact text NOT NULL )')

        Database.db.commit()
        print("Connected to DB successfully")

    @staticmethod
    def insertData(email, password):
        sql = "INSERT INTO users(email, password) VALUES (?, ?)"
        val = (f"{email}", f"{password}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        print("User added with success")

    # check to see if e-mail is present,
    # in this case returns False (invalid)
    # else returns True
    @staticmethod
    def isValid(email):
        sql = f"SELECT * FROM users WHERE email = '{email}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if (result):
            print("Email already in DB")
            return False
        else:
            return True

    # check to see if user is present,
    # in this case returns True
    # else returns False
    @staticmethod
    def exist(email, password):

        sql = f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if (result):
            print("User already in DB")
            return True
        else:
            return False

    @staticmethod
    def insertFact(id, email, fact):
        sql = "INSERT INTO fact_table(id, email, fact) VALUES (?, ?, ?)"
        val = (f"{id}", f"{email}", f"{fact}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()
        print("Fact added with success")

    @staticmethod
    def getFact(id, email):
        sql = f"select * from fact_table WHERE email = '{email}' AND id ='{id}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        fetch = cursor.fetchall()
        for item in fetch:
            id, mail, result = item
        result = (result + " ")*10
        print(result)
        if result:
            return result
        else:
            return False

    @staticmethod
    def getAllFact():
        sql = "select * from fact_table"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = ""
        fetch = cursor.fetchall()
        for item in fetch:
            id, mail, fact = item
            result += fact + "\n"
        print(result)
        if result:
            return result
        else:
            return False
