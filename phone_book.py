import psycopg2
import csv
from config import load_config

# Create the phonebook table
def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
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
                # Execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Insert data from CSV file
def insert_from_csv(file_path):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r') as f:
                    next(f)  # Skip header row
                    reader = csv.reader(f)
                    for row in reader:
                        cur.execute("""
                            INSERT INTO phonebook (first_name, last_name, phone_number)
                            VALUES (%s, %s, %s)
                        """, row)
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Insert data from console
def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO phonebook (first_name, last_name, phone_number)
                    VALUES (%s, %s, %s)
                """, (first_name, last_name, phone_number))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Update data in the table
def update_contact(phone_number, new_first_name=None, new_last_name=None, new_phone_number=None):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                query = "UPDATE phonebook SET "
                params = []
                
                if new_first_name:
                    query += "first_name = %s, "
                    params.append(new_first_name)
                if new_last_name:
                    query += "last_name = %s, "
                    params.append(new_last_name)
                if new_phone_number:
                    query += "phone_number = %s, "
                    params.append(new_phone_number)
                
                # Remove trailing comma and space
                query = query.rstrip(", ")

                query += " WHERE phone_number = %s"
                params.append(phone_number)

                cur.execute(query, tuple(params))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Query data from the table
def query_data(first_name=None, last_name=None, phone_number=None):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                query = "SELECT * FROM phonebook WHERE 1=1"
                params = []

                if first_name:
                    query += " AND first_name = %s"
                    params.append(first_name)
                if last_name:
                    query += " AND last_name = %s"
                    params.append(last_name)
                if phone_number:
                    query += " AND phone_number = %s"
                    params.append(phone_number)

                cur.execute(query, tuple(params))
                rows = cur.fetchall()

                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Delete data from the table by phone number
def delete_contact(phone_number):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone_number,))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
    # insert_from_csv('path_to_your_csv_file.csv')
    # insert_from_console()  # Uncomment to insert from console
    # update_contact('123-456-7890', new_first_name='John', new_phone_number='987-654-3210')
    # query_data(first_name='John')
    # delete_contact('123-456-7890')