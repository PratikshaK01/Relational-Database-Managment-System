import mysql.connector
import sys
sys.path.append('../EncryptorsDecryptors')
sys.path.append('../propertyFiles')
from encryptors import encrypt,decrypt
from properties import *




getSql = "SELECT Gr_no,rollNumber,firstName,surName,email,mobileNumber FROM student_info LIMIT 10;"


def InsertIntoDB(query):
    mydb=mysql.connector.connect(host='localhost',database='forms',user='root',password=decrypt(password))
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    mydb.close()
    print(mycursor.rowcount, "record inserted.")

def getQuery(query):
    mydb=mysql.connector.connect(host='localhost',database='forms',user='root',password=decrypt(password))
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    mydb.close()
    return result
# InsertIntoDB(sql)
result = getQuery(getSql)
# print(result)
