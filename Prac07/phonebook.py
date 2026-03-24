import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

def create_table():
    command = """CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20)
    )"""

    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()

def insert_contact(name, phone):
    command = "INSERT INTO contacts(name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        cur.execute(command, (name, phone))
        conn.commit()

def insert_contact_from_csv():
    command = "INSERT INTO contacts(name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        with open("contacts.csv", 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _ = next(csvreader)
            for row in csvreader:
                name, phone = row
                cur.execute(command, (name, phone))
        conn.commit()

def update_contacts_name(contact_id, new_name):
    command = "UPDATE contacts SET name = %s WHERE id = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new_name, contact_id))
        conn.commit()
        print(f"Updated {cur.rowcount} row(s)")

def update_contacts_phone(contact_id, new_phone):
    command = "UPDATE contacts SET phone = %s WHERE id = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new_phone, contact_id))
        conn.commit()
        print(f"Updated {cur.rowcount} row(s)")

def get_all_contacts():
    command = "SELECT * FROM contacts"
    with conn.cursor() as cur:
        cur.execute(command)
        return cur.fetchall()

def search_contacts_by_name(pattern):
    command = "SELECT * FROM contacts WHERE name LIKE %s"
    with conn.cursor() as cur:
        cur.execute(command, (f"%{pattern}%",))
        return cur.fetchall()

def search_contacts_by_phone_prefix(pattern):
    command = "SELECT * FROM contacts WHERE phone LIKE %s"
    with conn.cursor() as cur:
        cur.execute(command, (f"%{pattern}%",))
        return cur.fetchall()

def delete_contact_by_name(name):
    command = "DELETE FROM contacts WHERE name = %s"
    with conn.cursor() as cur:
        cur.execute(command, (name,))
        conn.commit()
        print(f"Deleted {cur.rowcount} row(s)")
    
def delete_contact_by_phone(phone):
    command = "DELETE FROM contacts WHERE phone = %s"
    with conn.cursor() as cur:
        cur.execute(command, (phone,))
        conn.commit()
        print(f"Deleted {cur.rowcount} row(s)")


create_table()

insert_contact_from_csv()

name = input("Enter name to insert: ")
phone = input("Enter phone to insert: ")
insert_contact(name, phone)

contact_id = input("Enter id to change name: ")
new_name = input("Enter new name: ")
update_contacts_name(contact_id, new_name)

contact_id = input("Enter id to change phone: ")
new_phone = input("Enter new phone: ")
update_contacts_phone(contact_id, new_phone)

print("All: ", get_all_contacts())

pattern = input("Enter pattern to search name: ")
print(f"Name contains {pattern}: ", search_contacts_by_name(pattern))

pattern = input("Enter pattern to search phone: ")
print(f"Phone contains {pattern}: ", search_contacts_by_phone_prefix(pattern))

name = input("Enter name to delete: ")
delete_contact_by_name(name)

phone = input("Enter phone to delete: ")
delete_contact_by_phone(phone)

print("All: ", get_all_contacts())
