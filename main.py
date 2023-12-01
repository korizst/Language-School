from database import create_table, get_entries, add_entry

welcome = 'Welcome to the management program of the Goethe Language School'

admin_menu = '''Please select one of the following options:
1) Add new admin
2) Add new teacher
3) Add new student
4) View admins
5) View teachers
6) View students
7) Exit

Your selection: '''  # Remember to add a DELETE option

teacher_menu = '''Please select one of the following options:
1) View my students
2) View all students
3) Exit

Your selection: '''

student_menu = '''Please select one of the following options:
1) View my data
2) Exit

Your selection: '''

def login():
    user_found = False
    while not user_found:
        username = input('Please enter your username: ')
        entries = get_entries()
        for entry in entries:
            if username == entry['username']:
                user_found = True
                password = input('Please enter your password: ')
                while password != entry['password']:
                    print('Wrong password, please try again!')
                    password = input('Please enter your password: ')
                if password == entry['password']:
                    print(f"Welcome back {entry['first_name']} {entry['surname']}")
                    user = [entry['permission'], entry["language"], entry['username']]
                    return user
        if not user_found:
            print('No such user found.')

def add_new_member():
    id_list = []
    entries = get_entries()
    for entry in entries:
        id_list.append(int(entry['id']))
    id = max(id_list) + 1
    first_name = input("First name: ")
    surname = input("Surname: ")
    username = first_name[0].lower() + surname.lower()
    password = f"12{first_name.lower()}34"
    if user_input == "1":
        permission = 'admin'
        language = ''
        fee_paid = 0
    elif user_input == "2":
        permission = 'teacher'
        language = input("Language: ")
        fee_paid = 0
    elif user_input == "3":
        permission = "student"
        language = input("Language: ")
        try:
            fee_paid = int(input("Fee paid: "))
        except ValueError:
            print("Invalid value. The paid fee will be 0.")
            fee_paid = 0
    add_entry(id, first_name, surname, username, password, permission, language, fee_paid)
    print(f"New {permission} added succesfully.")

def view_members():
    entries = get_entries()
    for entry in entries:
        if user[0] == 'admin':
            if user_input == '4' and entry['permission'] == 'admin':
                print(f"Id: {entry['id']}, Name: {entry['first_name']} {entry['surname']}")    
            elif user_input == '5' and entry['permission'] == 'teacher':
                print(f"Id: {entry['id']}, Name: {entry['first_name']} {entry['surname']}, Language: {entry['language']}")
            elif user_input == '6' and entry['permission'] == 'student':
                print(f"Id: {entry['id']}, Name: {entry['first_name']} {entry['surname']}, Language: {entry['language']}, paid fee: {entry['fee_paid']}")
        if user[0] == 'teacher':
            if user_input == '1' and entry['permission'] == 'student' and entry['language'] == user[1]:
                print(f"Name: {entry['first_name']} {entry['surname']}, Language: {entry['language']}")
            elif user_input == '2' and entry['permission'] == 'student':
                print(f"Name: {entry['first_name']} {entry['surname']}, Language: {entry['language']}")
        elif user[0] == 'student':
            if user[2] == entry["username"]:
                print(f"Name: {entry['first_name']} {entry['surname']}, Language: {entry['language']}, Paid fee: {entry['fee_paid']}")

create_table()
print(welcome)
user = login()
if user[0] == 'admin':
    while (user_input := input(admin_menu)) != "7":
        if user_input == "1":
            print("Adding new admin")
            add_new_member()
        elif user_input == "2":
            print("Adding new teacher")
            add_new_member()
        elif user_input == "3":
            print("Adding new student")
            add_new_member()
        elif user_input == "4":
            view_members()
        elif user_input == "5":
            view_members()
        elif user_input == "6":
            view_members()
        else:
            print('Invalid option. Please try again')
elif user[0] == 'teacher':
    while (user_input := input(teacher_menu)) != "3":
        if user_input == '1':
            view_members()
        elif user_input == '2':
            view_members()
        else:
            print('Invalid option. Please try again')
elif user[0] == 'student':
    while (user_input := input(student_menu)) != "2":
        if user_input == '1':
            view_members()
        else:
            print('Invalid option. Please try again')