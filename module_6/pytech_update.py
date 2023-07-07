# pytech_update.py

from pymongo import MongoClient
import random

url = "mongodb+srv://admin:admin@cluster0.cxxmeao.mongodb.net/"
client = MongoClient(url)
db = client['pytech'] # db pytech
students = db['students'] # collection students

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students.find():
    print(f'Student ID: {student["Student ID"]}\n'
            f'First Name: {student["First Name"]}\n'
            f'Last Name: {student["Last Name"]}\n')
    
# Random names to choose from whenever this script is run
last_names_list = ['Jones', 'Smith', 'Osteen', 'Erlich', 'Ruiz', 'Sharp', 'Ziegler', 'Fitkin', 'Olander', 'Johnson'] 
new_name = random.choice(last_names_list)

# Query and update student by ID
students.update_one({'Student ID': '1007'}, {'$set':{'Last Name': new_name}})

# Confirm update
student = students.find_one({'Student ID': '1007'})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print(f'Student ID: {student["Student ID"]}\n'
        f'First Name: {student["First Name"]}\n'
        f'Last Name: {student["Last Name"]}\n')