import mysql.connector as c 

con = c.connect(host="localhost", user="root", password="", database="gym")
mycursor = con.cursor()

# if con.is_connected():
#     print("successfully conected...")