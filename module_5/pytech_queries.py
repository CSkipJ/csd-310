# pytech_queries.py

from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--id', type=str, help='Queries the student collection for one 4-digit ID.')
args = parser.parse_args()


url = "mongodb+srv://admin:admin@cluster0.cxxmeao.mongodb.net/"
client = MongoClient(url)
db = client['pytech']
students = db['students']


# print(coll.find({'Student ID': '1007'}))

if args.id == None: # defaults to returning all objects in student collection
    for student in students.find():
        print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
        print(f'Student ID: {student["Student ID"]}\n'
              f'First Name: {student["First Name"]}\n'
              f'Last Name: {student["Last Name"]}\n')
elif args.id:
    try:
        student = students.find_one({'Student ID': args.id})
        print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
        print(f'Student ID: {student["Student ID"]}\n'
              f'First Name: {student["First Name"]}\n'
              f'Last Name: {student["Last Name"]}\n')
    except:
        print('Something went wrong. Record may not exist.')

print("End of program, press any key to continue...")
