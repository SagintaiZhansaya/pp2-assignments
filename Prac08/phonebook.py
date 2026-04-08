import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
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



def upsert_contacts(p_name, p_phone):
    command = "CALL upsert_contacts(%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (p_name, p_phone))
            conn.commit()
            print(f"Upserted: {p_name} {p_phone}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def bulk_insert_contacts(names, phones):
    command = "CALL bulk_insert_contacts(%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (names, phones))
            conn.commit()
            print(f"Bulk insert done ({len(names)} entries processed)")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def search_contacts(pattern):
    command = "SELECT * FROM search_contacts(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (pattern,))
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def get_contacts_page(page_limit, page_offset):
    command = "SELECT * FROM get_contacts_page(%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (page_limit, page_offset))
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def delete_by_name(name_to_delete):
    command = "CALL delete_by_name(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name_to_delete,))
            conn.commit()
            print(f"Deleted contact with name: {name_to_delete}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def delete_by_phone(phone_to_delete):
    command = "CALL delete_by_phone(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (phone_to_delete,))
            conn.commit()
            print(f"Deleted contact with phone: {phone_to_delete}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

create_table()


p_name = input("Enter name: ")
p_phone = input("Enter phone: ")
upsert_contacts(p_name, p_phone)


names = []
phones = []
n = int(input("Number of contacts to add: "))
for _ in range(n):
    names.append(input("Name: "))
    phones.append(input("Phone: "))
bulk_insert_contacts(names, phones)


pattern = input("Search pattern: ")
results = search_contacts(pattern)
print("Found:", results)


page_offset = int(input("Enter offset number: "))
page_limit = int(input("Enter limit number: "))
page = get_contacts_page(page_limit, page_offset)
print(page)


name_to_delete = input("Enter name to delete: ")
delete_by_name(name_to_delete)

phone_to_delete = input("Enter phone to delete: ")
delete_by_phone(phone_to_delete)

conn.close()