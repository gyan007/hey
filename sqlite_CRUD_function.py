import sqlite3

# --- 1️ Connect to database (or create one if it doesn't exist) ---
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# --- 2️ Create table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')
conn.commit()

# --- 3️ CREATE (Insert) ---
def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print(" Student added successfully!")

# --- 4️ READ (Select) ---
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# --- 5️ UPDATE ---
def update_student(student_id, name, age, grade):
    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    conn.commit()
    print(" Student updated successfully!")

# --- 6️ DELETE ---
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print(" Student deleted successfully!")

# --- 7️ Example usage ---
if __name__ == "__main__":
    add_student("Alice", 20, "A")
    add_student("Bob", 22, "B")
    print("\n All students:")
    view_students()

    print("\n Updating Bob's record...")
    update_student(2, "Bob Marley", 23, "A+")

    print("\n Students after update:")
    view_students()

    print("\n Deleting Alice...")
    delete_student(1)

    print("\n Final student list:")
    view_students()

# --- 8️ Close connection ---
conn.close()
