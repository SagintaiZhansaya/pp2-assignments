import psycopg2
import json
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

def initialize_db():
    try:
        with conn.cursor() as cur:
            with open('schema.sql', 'r', encoding='utf-8') as f:
                cur.execute(f.read())

            with open('procedures.sql', 'r', encoding='utf-8') as f:
                cur.execute(f.read())
    
            conn.commit()
            print("SQL files successfully uploaded.")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

initialize_db()


def filter_by_group(group_name):
    command = """
        SELECT c.name, c.email, g.name 
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """

    with conn.cursor() as cur:
        cur.execute(command, (group_name,))
        return cur.fetchall()
    

def search_by_email(pattern):
    command = "SELECT name, email FROM contacts WHERE email ILIKE %s"
    like_pattern = f"%{pattern}%"
    
    with conn.cursor() as cur:
        cur.execute(command, (like_pattern,))
        return cur.fetchall()


def sort_contacts():
    print("Select sorting type: 1 - by name, 2 - by birthday, 3 - by date added")
    choice = input()
    sort_map = {"1": "name", "2": "birthday", "3": "id"}
    column = sort_map.get(choice, "name")
    command = f"SELECT name, email, birthday FROM contacts ORDER BY {column} ASC"

    with conn.cursor() as cur:
        cur.execute(command)
        return cur.fetchall()
    

def paginated_view():
    limit = 5
    offset = 0
    
    while True:
        command = "SELECT id, name FROM contacts ORDER BY id LIMIT %s OFFSET %s"
        with conn.cursor() as cur:
            cur.execute(command, (limit, offset))
            return cur.fetchall()
        
        if not contacts and offset > 0:
            print("No more contacts")
            offset -= limit
            continue

        print(f"Current page {(offset // limit) + 1}")
        for c in contacts:
            print(f"{c[0]} : {c[1]}")
            
        print("Commands: next, prev, quit")
        cmd = input().lower()
        
        if cmd == 'next':
            offset += limit
        elif cmd == 'prev':
            if offset >= limit:
                offset -= limit
        elif cmd == 'quit':
            break


def export_to_json(filename):
    command = """
        SELECT c.id, c.name, c.email, c.birthday, g.name as group_name 
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """
    with conn.cursor() as cur:
        cur.execute(command)
        rows = cur.fetchall()
    
    data = []

    for c_id, name, email, bday, g_name in contacts:
        cur.execute("SELECT phone, type FROM phones WHERE contact_id = %s", (c_id,))
        phones_rows = cur.fetchall()
        phones_list = [{"number": p[0], "type": p[1]} for p in phones_rows]
        
        data.append({
            "name": name,
            "email": email,
            "birthday": str(bday) if bday else None,
            "group": g_name,
            "phones": phones_list  
        })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully exported {len(data)} contacts to file {filename}!")


def import_from_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found!")
        return

    cur = conn.cursor()
    for entry in data:
        cur.execute("SELECT id FROM contacts WHERE name = %s", (entry['name'],))
        existing_contact = cur.fetchone()
        
        if existing_contact:
            print(f"Contact '{entry['name']}' already exists.")
            choice = input("skip or overwrite").lower()
            if choice == 'skip':
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE id = %s", (existing_contact[0],))
        
        if entry.get('group'):
            cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (entry['group'],))
            cur.execute("SELECT id FROM groups WHERE name = %s", (entry['group'],))
            group_id = cur.fetchone()[0]
        else:
            group_id = None

        cur.execute(
            "INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
            (entry['name'], entry.get('email'), entry.get('birthday'), group_id)
        )
    
        new_contact_id = cur.fetchone()[0]
        phones = entry.get('phones', [])
        for p in phones:
            cur.execute(
                "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                (new_contact_id, p.get('number'), p.get('type', 'mobile'))
            )
    conn.commit()
    print("Import complete!")


def import_from_csv(csv_file_name):
    insert_group = "INSERT INTO groups(name) VALUES(%s) ON CONFLICT (name) DO NOTHING"
    get_group_id = "SELECT id FROM groups WHERE name = %s"
    insert_contact = "INSERT INTO contacts(name, email, birthday, group_id) VALUES(%s, %s, %s, %s) RETURNING id"
    insert_phone = "INSERT INTO phones(contact_id, phone, type) VALUES(%s, %s, %s)"

    with conn.cursor() as cur:
        with open(csv_file_name, "r", encoding="utf-8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _ = next(csvreader) 
            
            for row in csvreader:
                name, email, birthday, group_name, phone_number, phone_type = row
                
                group_id = None
                if group_name:
                    cur.execute(insert_group, (group_name,))
                    cur.execute(get_group_id, (group_name,))
                    group_id = cur.fetchone()[0]

                cur.execute(insert_contact, (name, email, birthday or None, group_id))
                contact_id = cur.fetchone()[0]

                if phone_number:
                    cur.execute(insert_phone, (contact_id, phone_number, phone_type or 'mobile'))
        conn.commit()
    print(f"Data from {csv_file_name} imported successfully!")


def add_phone_to_contact(name, phone, phone_type):
    try:
        with conn.cursor() as cur:
            cur.execute("CALL add_phone(%s, %s, %s);", (name, phone, phone_type))
            conn.commit()
            print(f"The number {phone} has been successfully added to the contact {name}!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def change_contact_group(contact_name, group_name):
    try:
        with conn.cursor() as cur:
            cur.execute("CALL move_to_group(%s, %s);", (contact_name, group_name))
            conn.commit()
            print(f"Contact {contact_name} has been moved to the group {group_name}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def global_search(query):
    command = "SELECT * FROM search_contacts(%s);"
    
    with conn.cursor() as cur:
        cur.execute(command, (query,))
        results = cur.fetchall()
        
        if not results:
            print("Nothing found.")
            return []
            
        print(f"Matches found: {len(results)}")
        return results

def main():
    while True:
        print("\n---Phonebook---")
        print("1. Import from JSON")
        print("2. Export to JSON")
        print("3. Import from CSV")
        print("4. Add phone to contact")
        print("5. Move a contact to a different group")
        print("6. Search contact")
        print("7. Search contact by email")
        print("8. Filter by group")
        print("9. Sort results")
        print("10. Paginated navigation")
        print("0. Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            import_from_json("contacts_import.json")
        elif choice == "2":
            export_to_json("contacts_export.json")
        elif choice == "3":
            import_from_csv("contacts_importcsv.csv")
        elif choice == "4":
            name = input("\nName: ")
            phone = input("\nPhone: ")
            phone_type = input("\nPhone type: ")
            add_phone_to_contact(name, phone, phone_type)
        elif choice == "5":
            contact_name = input("\nContact name: ")
            group_name = input("\nGroup name: ")
            change_contact_group(contact_name, group_name)
        elif choice == "6":
            query = input("\nPattern to search: ")
            global_search(query)
        elif choice == "7":
            pattern = input("\nPattern for email: ")
            search_by_email(pattern)
        elif choice == "8":
            group_name = input("\nGroup name: ")
            filter_by_group(group_name)
        elif choice == "9":
            sort_contacts()
        elif choice == "10":
            paginated_view()
        elif choice == "0":
            break
        else:
            print("Invalid choice")
    
    conn.close()
    print("Good bye!")


if __name__ == "__main__":
    main()