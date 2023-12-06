import sqlite3

conn = sqlite3.connect('staff_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        address TEXT NOT NULL,
        qualifications TEXT,
        role TEXT,
        contact_number TEXT
    )
''')
conn.commit()

def add_staff():
    name = input("Enter the name: ")
    email = input("Enter the e-mail id: ")
    age = int(input("Enter the age: "))
    address = input("Enter the address: ")
    qualifications = input("Enter the qualifications: ")
    role = input("Enter the role: ")
    contact_number = input("Enter the contact number: ")

    cursor.execute('''
        INSERT INTO staff (name, email, age, address, qualifications, role, contact_number)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, age, address, qualifications, role, contact_number))
    conn.commit()
    print("Staff information added successfully.")

def view_staff():
    cursor.execute('SELECT * FROM staff')
    rows = cursor.fetchall()
    if not rows:
        print("No staff information available.")
    else:
        for row in rows:
            print(row)

def update_staff():
    staff_id = int(input("Enter the staff ID to update: "))
    name = input("Enter the new name: ")
    email = input("Enter the e-mail id: ")
    age = int(input("Enter the new age: "))
    address = input("Enter the new address: ")
    qualifications = input("Enter the new qualification: ")
    role = input("Enter the new role: ")
    contact_number = input("Enter the contact new number: ")

    cursor.execute('''
        UPDATE staff
        SET name = ?, email = ?, age = ?, address = ?, qualifications = ?, role = ?, contact_number = ? 
        WHERE id = ?
    ''', (name,email,age,address,qualifications,role,contact_number,staff_id))
    conn.commit()
    print("Staff information updated successfully.")

def delete_staff():
    staff_id = int(input("Enter the staff ID to delete: "))

    cursor.execute('DELETE FROM staff WHERE id = ?', (staff_id,))
    conn.commit()
    print("Staff information deleted successfully.")

while True:
    print("\nStaff Management System")
    print("1. Add Staff")
    print("2. View Staff")
    print("3. Update Staff")
    print("4. Delete Staff")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_staff()
    elif choice == '2':
        view_staff()
    elif choice == '3':
        update_staff()
    elif choice == '4':
        delete_staff()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

conn.close()