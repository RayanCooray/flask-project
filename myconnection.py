## mysql connector

import mysql.connector as connector

myDataBase = connector.connect(
    host = "database-1.cxo8imqa00uc.us-east-1.rds.amazonaws.com",
    user = "admin",
    passwd = "ijse1234",
)

print(myDataBase)