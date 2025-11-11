# pip install pymongo

from pymongo import MongoClient

# 1️ Connect to MongoDB (local instance)
client = MongoClient("mongodb://localhost:27017/")

# 2️ Create (or switch to) a database
db = client["school"]

# 3️ Create (or switch to) a collection (like a table)
students = db["students"]

# --- CREATE ---
student1 = {"name": "Alice", "age": 20, "grade": "A"}
student2 = {"name": "Bob", "age": 22, "grade": "B"}
students.insert_many([student1, student2])
print(" Students added successfully!")

# --- READ ---
print("\n All students:")
for s in students.find():
    print(s)

# --- UPDATE ---
students.update_one({"name": "Bob"}, {"$set": {"grade": "A+"}})
print("\n Bob's record updated!")

# --- READ AGAIN ---
print("\n Updated student list:")
for s in students.find():
    print(s)

# --- DELETE ---
students.delete_one({"name": "Alice"})
print("\n Alice deleted!")

# --- FINAL VIEW ---
print("\n Final students in collection:")
for s in students.find():
    print(s)

