"""Homework_lesson_8
Book classidagi crud amalini context manager orqali yozasizlar
"""
import psycopg2
from colorama import Fore

db_case = {
    'dbname': 'school',
    'user': 'postgres',
    'host': 'localhost',
    'port': 5432,
    'password': '1234',
}


class MyDatabaseConnect:
    def __init__(self, db_case):
        self.db_case = db_case

    def __enter__(self):
        self.conn = psycopg2.connect(**db_case)
        self.cursor = self.conn.cursor()
        return self.conn, self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor and not self.cursor.closed:
            self.cursor.close()

        if self.conn and not self.conn.closed:
            self.conn.close()


with MyDatabaseConnect(db_case) as (conn, cursor):
    def execute_query(query: str | list) -> None:
        cursor.execute(query)


    def connect_to_db() -> None:
        conn.commit()


    def fetch_data() -> None:
        cursor.fetchall()


    def create_table() -> None:
        create_table_query = '''CREATE TABLE IF NOT EXISTS students (
                                id SERIAL PRIMARY KEY,
                                username VARCHAR(255) NOT NULL,
                                address TEXT,
                                email VARCHAR(255) NOT NULL,
                                age INT NOT NULL,
                                UNIQUE(email),
                                CHECK (age > 0))'''
        execute_query(create_table_query)
        connect_to_db()


    def insert_data() -> None:
        insert_data_query = '''INSERT INTO students (username, email, age)
                               VALUES ('John Doe', 'john035@gmail.com', '34'),
                                      ('Jane Ward', 'jane03@gmail.com', '28'),
                                      ('Jack Doe', 'jack010@gmail.com', '41'),
                                      ('Sharafbek Dehqonov', 'sharaf7003@gmail.com', '21')'''
        execute_query(insert_data_query)
        connect_to_db()


    def fetch_data_from_table() -> None:
        select_fetch_query = """SELECT * FROM public.students;"""

        execute_query(select_fetch_query)
        rows = cursor.fetchall()
        # print(f'{rows} \n')
        for row in rows:
            print(row)


    def update_data_from_table() -> None:
        update_data_query = """UPDATE students SET username = %s, email =%s, age = %s WHERE id = %s;"""

        update_data = ('Leo Messi', 'leo@gmail.com', 37, 3)
        cursor.execute(update_data_query, update_data)
        conn.commit()


    def delete_data_from_table() -> None:
        delete_data_query = '''DELETE FROM students WHERE id = 2;'''
        execute_query(delete_data_query)
        connect_to_db()


    def my_data_menu() -> None:
        message: str = input(Fore.GREEN + 'Do you want to choice database? [y/n] => ' + Fore.RESET)

        while 'y' in message:
            print(Fore.MAGENTA + 'This is menu. Choice your category😎.' + Fore.RESET +
                  Fore.GREEN + '\n1 => Create table' +
                  '\n2 => Insert data' +
                  '\n3 => Fetch data from table' +
                  '\n4 => Update data from table' +
                  '\n5 => Delete data from table' + Fore.RESET)

            try:
                choice = int(input(Fore.GREEN + 'Enter your choice: ' + Fore.RESET))
                for choice in range(1, 6):
                    if choice == 1:
                        create_table()
                    if choice == 2:
                        insert_data()
                    if choice == 3:
                        fetch_data_from_table()
                    if choice == 4:
                        update_data_from_table()
                    if choice == 5:
                        delete_data_from_table()

            except Exception:
                print(Fore.RED + 'You have entered an invalid choice. Please try again.' + Fore.RESET)

            message: str = input(Fore.GREEN + 'Do you want to choice database? [y/n] => ' + Fore.RESET)


    if __name__ == '__main__':
        my_data_menu()
