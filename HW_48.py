import psycopg2

def create_db_structure():
    conn = psycopg2.connect(host='localhost', user='postgres', password='password', database='postgres')
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE clients_db")
    cursor.close()
    conn.close()

    conn = psycopg2.connect(host='localhost', user='postgres', password='password', database='clients_db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE clients (
            client_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE phones (
            phone_id SERIAL PRIMARY KEY,
            client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
            phone_number VARCHAR(20)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


def add_client(first_name, last_name, email):
    conn = psycopg2.connect(host='localhost', user='postgres', password='password', database='clients_db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO clients (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING client_id",
                   (first_name, last_name, email))
    client_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()
    return client_id


def add_phone(client_id, phone_number):
    conn = psycopg2.connect(host='localhost', user='postgres', password='password', database='clients_db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO phones (client_id, phone_number) VALUES (%s, %s)",
                   (client_id, phone_number))

    conn.commit()
    cursor.close()
    conn.close()


def update_client(client_id, first_name=None, last_name=None, email=None):
    conn = psycopg2.connect(host='localhost', user='postgres', password='password', database='clients_db')
    cursor = conn.cursor()

    if first_name:
        cursor.execute("UPDATE clients SET first_name = %s WHERE client_id = %s", (first_name, client_id))
    if last_name:
        cursor.execute("UPDATE clients SET last_name = %s WHERE client_id = %s", (last_name, client_id))
    if email:
        cursor.execute("UPDATE clients SET email = %s WHERE client_id = %s", (email, client_id))

    conn.commit()
    cursor.close()
    conn.close()

def delete_phone(client_id, phone_number):
    conn = psycopg2.connect(host='localhost', user='postgres', password='password', database='clients_db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM phones WHERE client_id = %s AND phone_number = %s",
                   (client_id, phone_number))

    conn.commit()
    cursor.close()
    conn.close()

def delete_client(client_id):
    conn = psycopg2.connect(host='localhost', user='postgres', password='password', database='clients_db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clients WHERE client_id = %s", (client_id,))

    conn.commit()
    cursor.close()
    conn.close()

def find_client(search_term):
    conn = psycopg2.connect(host='localhost', user='postgres', password='password', database='clients_db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.client_id, c.first_name, c.last_name, c.email, p.phone_number 
        FROM clients c 
        LEFT JOIN phones p ON c.client_id = p.client_id 
        WHERE c.first_name = %s OR c.last_name = %s OR c.email = %s OR p.phone_number = %s
    """, (search_term, search_term, search_term, search_term))

    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

create_db_structure()

client1 = add_client("Иван", "Иванов", "ivan@mail.ru")
add_phone(client1, "+79161234567")
add_phone(client1, "+79167654321")

client2 = add_client("Петр", "Петров", "petr@mail.ru")
add_phone(client2, "+79031112233")

update_client(client1, first_name="Иван", last_name="Сидоров")

delete_phone(client1, "+79167654321")

search_results = find_client("Иванов")
search_results2 = find_client("+79031112233")

delete_client(client2)