from datetime import datetime
import sqlite3
import bcrypt

connection = sqlite3.connect('competency_tracker.db')
cursor = connection.cursor()

with open('create_tables.txt', 'r') as readfile:
    cursor.executescript(readfile.read())


user_fields = ['user_id', 'first_name', 'last_name', 'phone', 'email', 'password', 'active', 'date_created', 'hire_date', 'user_type']
user_titles = ['User ID', 'First Name', 'Last Name', 'Phone', 'Email', 'Password', 'Active', 'Date Created', 'Hire Date', 'User Type']
user_widths = [10, 15, 15, 15, 25, 20, 8, 14, 12, 11]

def sanitize(response, valid_options):
    while response not in valid_options:
        response = input("Invalid Input. Enter valid menu response: ")
    return response


def view_rows(table, fields, titles, widths, rows='', active=True):
    if not rows:
        if active:
            query = f"SELECT {','.join(fields)} FROM {table} WHERE active = 1"
        else:
            query = f"SELECT {','.join(fields)} FROM {table}"

        rows = cursor.execute(query)

    for i in range(len(titles)): print(f"{titles[i]:<{widths[i]}}", end='')
    print()
    for row in rows:
        for i in range(len(row)): print(f"{row[i]:<{widths[i]}}", end='')
        print()


def add_record(table, fields, titles, widths):
    values_list = []
    for title in titles[1:-1]:
        values_list.append(input(f"{title}: "))

    query = f"INSERT INTO {table} ({','.join(fields[1:-1])}) VALUES (?{',?'*(len(fields[1:-1])-1)})"
    values = tuple(values_list)

    cursor.execute(query, values)
    connection.commit()

    added_row = cursor.execute(f"SELECT * FROM {table} ORDER BY {fields[0]} DESC LIMIT 1").fetchall()

    print("\n\nNew Record Added Successfully!\n\n")
    view_rows(table, fields, titles, widths, added_row)


def update_record(table, fields, titles, widths):
    while True:
        update_menu_response = input(f'''
V] View all active {table}
Q] Exit Menu
Enter {titles[0]}: ''').lower()

        available_ids = [row[0] for row in cursor.execute(f"SELECT {fields[0]} FROM {table}").fetchall()]
        while update_menu_response not in ['v', 'q', ''] and int(update_menu_response) not in available_ids:
            update_menu_response = input("Invalid Input.\nEnter a menu option or valid ID: ").lower()

        if update_menu_response == 'v':
            view_rows(table, fields, titles, widths)
        elif update_menu_response not in ['q', '']:
            row_to_update = cursor.execute(f"SELECT * FROM {table} WHERE {fields[0]} = ?", (update_menu_response,)).fetchone()

            for i in range(len(titles[:-1])):
                print(f"{i+1} - {titles[i]}: {row_to_update[i]}")

            update_field_response = input("Select field to Update: ").lower()
            while not update_field_response.isnumeric() and (update_field_response not in ['', 'q'] and int(update_field_response) not in range(len(titles[:-1]))):
                update_field_response = input("Select a valid field by number to update: ").lower()

            if update_field_response == '1':
                print("ID fields cannot be updated.\n")
                continue
            if update_field_response in ['q', '']:
                continue

            ufr = int(update_field_response) - 1
            print(f"Current {titles[ufr]}: {row_to_update[ufr]}")
            new_value = input(f"Enter new {titles[ufr]}: ")
            if not new_value: continue

            if fields[ufr] == "email":
                taken_emails = [row[0] for row in cursor.execute(f"SELECT email FROM Users").fetchall()]
                while new_value in taken_emails:
                    new_value = input(f"Email address unavailable, please use another email address: ")

            cursor.execute(f"UPDATE {table} SET {fields[ufr]} = ? WHERE {fields[0]} = ?", (new_value, update_menu_response))
            connection.commit()

            print(f"Successfully Updated {table} Table")
            updated_row = cursor.execute(f"SELECT * FROM {table} WHERE {fields[0]} = ?", (update_menu_response,)).fetchall()
            view_rows(table, fields, titles, widths, updated_row)
            input()
        else:
            break


def users_menu():
    while True:
        users_menu_response = sanitize(input('''>>>> Courses Menu <<<<

1] View All Users
2] Add New User
3] Update User
4] Add Assessment Result
5] Edit Assessment Result
6] Delete Assessment Result
7] Return to Menu
''').lower(), ['1','2','3','4','5','6','7','v','a','u','s','e','d','r'])

        if users_menu_response in ['1', 'v']:
            view_rows('Users', user_fields, user_titles, user_widths)
        elif users_menu_response in ['2', 'a']:
            add_record('Users', user_fields, user_titles, user_widths)
        elif users_menu_response in ['3', 'd']:
            update_record('Users', user_fields, user_titles, user_widths)
        else:
            break

def assessments_menu():
    while True:
        assessments_menu_response = sanitize(input('''>>>> Courses Menu <<<<

1] View All Assessments
2] Add New Assessment
3] Update Assessment
4] Return to Menu
''').lower(), ['1','2','3','4','v','a','u','r'])

        if assessments_menu_response in ['1', 'v']:
            view_rows()
        elif assessments_menu_response in ['2', 'a']:
            add_record()
        elif assessments_menu_response in ['3', 'd']:
            update_record()
        else:
            break


def competencies_menu():
    while True:
        competency_menu_response = sanitize(input('''>>>> Courses Menu <<<<

1] View All Competencies
2] Add New Competency
3] Update Competency
4] Return to Menu
''').lower(), ['1','2','3','v','a','u'])

        if competency_menu_response in ['1', 'v']:
            view_rows()
        elif competency_menu_response in ['2', 'a']:
            add_record()
        elif competency_menu_response in ['3', 'd']:
            update_record()
        else:
            break


while True:
    main_menu_response = sanitize(input('''
********** Welcome to **********
*** Something Else Application ***

1] Users
2] Assessments
3] Competencies
4] Quit

Select a menu: ''').lower(), ['1','2','3','4','u','a','c','q'])

    if main_menu_response in ['1', 'u']:
        users_menu()
    elif main_menu_response in ['3', 'a']:
        assessments_menu()
    elif main_menu_response in ['4', 'c']:
        competencies_menu()
    else:
        break

print('''**** Thank You ****
*** Come again!!***''')