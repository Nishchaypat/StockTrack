import sys
import mysql.connector

class sql_connector():

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="",database="stocktrack")
            self.mycursor = self.conn.cursor()

        except Exception as e:
            print("Some error occured:", e)
            sys.exit(0)

    def register(self, firstname, lastname, email, password):
        try:
            self.mycursor.execute("""
                INSERT INTO users (firstname, lastname, email, password) 
                VALUES (%s, %s, %s, %s);
            """, (firstname, lastname, email, password))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def search(self, email, password):
        try:
            self.mycursor.execute("""
                SELECT * FROM users 
                WHERE email = %s AND password = %s;
            """, (email, password))
            data = self.mycursor.fetchall()
            return data
        except Exception as e:
            print(f"Error: {e}")
            return False

