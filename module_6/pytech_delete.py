# pytech_delete.py

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.cxxmeao.mongodb.net/"
client = MongoClient(url)
db = client['pytech'] # db pytech
students = db['students'] # collection students

# Display all records
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students.find():
    print(f'Student ID: {student["Student ID"]}\n'
            f'First Name: {student["First Name"]}\n'
            f'Last Name: {student["Last Name"]}\n')

# New record to be added and deleted
std_rcd = {
    'Student ID': '1010',
    'First Name': 'Elizabeth',
    'Last Name': 'Wright'
}

# Inserted record and stored id
new_student_id = students.insert_one(std_rcd).inserted_id
print('-- INSERT STATEMENTS --')
print(f"Inserted student record Elizabeth Wright into the students collection with document_id", new_student_id)
print()

# Confirm record added
student = students.find_one({'Student ID': '1010'})
print("-- DISPLAYING STUDENTS TEST DOC --")
print(f'Student ID: {student["Student ID"]}\n'
        f'First Name: {student["First Name"]}\n'
        f'Last Name: {student["Last Name"]}\n')

# Delete added record
students.delete_one({'Student ID': '1010'})

# Confirm Deletion
for student in students.find():
    print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
    print(f'Student ID: {student["Student ID"]}\n'
            f'First Name: {student["First Name"]}\n'
            f'Last Name: {student["Last Name"]}\n')
