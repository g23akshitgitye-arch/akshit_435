from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData
def insert():
   try:
       employeeID = input('Enter Employee ID:')
       employeeName = input('Enter Name:')
       employeeAge = input('Enter age:')
       employeeCountry = input('Enter country')


       db.Employees.insert_one(
           {
               "id":employeeID,
               "name":employeeName,
               "age":employeeAge,
               "country":employeeCountry
           }
       )
       print("\n Insert successfully\n")
   except Exception as e:
       print(str(e))
insert()   
