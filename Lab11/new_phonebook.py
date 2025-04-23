import psycopg2
import csv
from config import load_config

# Create the phonebook11 table
def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook11 (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100),
            phone_number VARCHAR(15) NOT NULL UNIQUE
        )
        """,
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error creating tables:", error)

# Insert from CSV
def insert_from_csv(file_path):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r') as f:
                    next(f)
                    reader = csv.reader(f)
                    for row in reader:
                        cur.execute("""
                            INSERT INTO phonebook11 (first_name, last_name, phone_number)
                            VALUES (%s, %s, %s)
                            ON CONFLICT (phone_number) DO NOTHING
                        """, row)
                conn.commit()
    except Exception as error:
        print("Error inserting from CSV:", error)

# Insert from console
def insert_from_console():
    fname = input("First name: ")
    lname = input("Last name: ")
    pnum = input("Phone number: ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO phonebook11 (first_name, last_name, phone_number)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (phone_number) DO NOTHING
                """, (fname, lname, pnum))
                conn.commit()
    except Exception as error:
        print("Error inserting from console:", error)

# Update contact
def update_contact(phone_number, new_fname=None, new_lname=None, new_pnum=None):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                query = "UPDATE phonebook11 SET "
                params = []

                if new_fname:
                    query += "first_name = %s, "
                    params.append(new_fname)
                if new_lname:
                    query += "last_name = %s, "
                    params.append(new_lname)
                if new_pnum:
                    query += "phone_number = %s, "
                    params.append(new_pnum)

                query = query.rstrip(', ')
                query += " WHERE phone_number = %s"
                params.append(phone_number)

                cur.execute(query, tuple(params))
                conn.commit()
    except Exception as error:
        print("Error updating contact:", error)

# Query data with filters
def query_data(fname=None, lname=None, pnum=None):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                query = "SELECT * FROM phonebook11 WHERE 1=1"
                params = []

                if fname:
                    query += " AND first_name = %s"
                    params.append(fname)
                if lname:
                    query += " AND last_name = %s"
                    params.append(lname)
                if pnum:
                    query += " AND phone_number = %s"
                    params.append(pnum)

                cur.execute(query, tuple(params))
                for row in cur.fetchall():
                    print(row)
    except Exception as error:
        print("Error querying data:", error)

# Delete contact by name or phone
def delete_contact(name=None, phone=None):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if name:
                    cur.execute("DELETE FROM phonebook11 WHERE first_name = %s", (name,))
                elif phone:
                    cur.execute("DELETE FROM phonebook11 WHERE phone_number = %s", (phone,))
                conn.commit()
    except Exception as error:
        print("Error deleting contact:", error)

def search_by_pattern(pattern):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM phonebook11 
                    WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone_number ILIKE %s 
                    ORDER BY user_id
                """, (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Search error:", e)

# Insert or update single user
def insert_or_update_user(first_name, last_name, phone):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO phonebook11 (first_name, last_name, phone_number)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (phone_number) DO UPDATE
                    SET first_name = EXCLUDED.first_name,
                        last_name = EXCLUDED.last_name
                """, (first_name, last_name, phone))
                conn.commit()
                print(f"{first_name} {last_name} inserted or updated.")
    except Exception as e:
        print("Insert/Update error:", e)

# Insert multiple users
def insert_many_users(data_list):
    try:
        config = load_config()
        invalid = []
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for first_name, last_name, phone in data_list:
                    if not phone.isdigit() or len(phone) < 10:
                        invalid.append((first_name, last_name, phone))
                        continue
                    cur.execute("""
                        INSERT INTO phonebook11 (first_name, last_name, phone_number)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (phone_number) DO UPDATE
                        SET first_name = EXCLUDED.first_name,
                            last_name = EXCLUDED.last_name
                    """, (first_name, last_name, phone))
                conn.commit()
                if invalid:
                    print("Invalid entries:", invalid)
                else:
                    print("All users inserted or updated.")
    except Exception as e:
        print("Batch insert error:", e)

# Pagination query
def query_pagination(limit, offset):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM phonebook11 
                    ORDER BY user_id 
                    LIMIT %s OFFSET %s
                """, (limit, offset))
                for row in cur.fetchall():
                    print(row)
    except Exception as e:
        print("Pagination query error:", e)


if __name__ == '__main__':
    create_tables()
    #insert_from_csv("users.csv")
    #insert_from_console()
    update_contact("87077211101", new_fname="Amina", new_pnum="87019910542")
    #query_data(fname="Sabina")
    #delete_contact(name="Amina")
    #insert_or_update_user("Amina", "Ali", "87077211101")
    users = [
        ("Sabina", "Khan", "87011110001"),
        ("Timur", "Bek", "87011110002"),
        ("Aliya", "Nur", "8701111BAD"),
    ]
    #insert_many_users(users)
    #search_by_pattern("Ali")
    #query_pagination(limit=2, offset=0)

