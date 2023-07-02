# pytech_insert.py

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.cxxmeao.mongodb.net/"
client = MongoClient(url)
db = client['pytech']
students = db['students']

std_id = input("Student ID: ")
first_name = input("First Name: ")
last_name = input("Last Name: ")

std_rcd = {
    'Student ID': std_id,
    'First Name': first_name,
    'Last Name': last_name
}

try:
    new_student_id = students.insert_one(std_rcd).inserted_id
    print(f"Inserted student record {first_name} {last_name} into the students collection with document_id", new_student_id)
except:
    print("Something went wrong. Record not added.")    

print("End of program, press any key to continue...")
