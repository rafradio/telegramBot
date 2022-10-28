import mysql.connector

class FormToMSQLQuery:
    def __init__(self, passwordMySQL):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=passwordMySQL,
            database="database3"
        )
        self.mycursor = self.mydb.cursor()
        # self.MySQLCommands()

    def MySQLCommands(self, sqlQuery):
        sql = sqlQuery
        self.mycursor.execute(sql)
        myAllData = self.mycursor.fetchall()
        self.commands = [x[1] for x in myAllData]

    def MySQLFindAnswer(self, sqlQuery):
        sql = sqlQuery
        print(sql)
        self.mycursor.execute(sql)
        myAllData = self.mycursor.fetchone()
        self.answer = myAllData[2]
        
        
