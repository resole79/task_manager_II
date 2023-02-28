#=====importing libraries===========
'''This is the section where you will import libraries'''
#import  os
import datetime
from datetime import date

# Declare variable
today = datetime.datetime.today()

# Function
# Function to display statistic
def display_statistic() :
    # Call the function "read_file" to open "task_overview.txt" and "user_overview.txt"
    task_overwiew_file = read_file(file3)
    user_overwiew_file = read_file(file4)
    #print(task_overwiew_file)

    # Print out statistic
    print('\nUser statistics : \n')
    # Cycle "for" to read user statistic
    for read_user_stat in user_overwiew_file:
        for user_stat in read_user_stat:
            print(user_stat)

    # Cycle "for" to read tasks stat
    print('\nTasks statistics : \n')
    # Cycle "for" to read task statistic
    for read_task_stat in task_overwiew_file:
        for task_stat in read_task_stat:
            print(task_stat)
# Function to generate report
def generate_report(voice_menu="gr") :
    # Declare Variable
    count_tasks_no_completed = 0
    count_tasks_completed = 0
    count_tasks_overdue = 0

    # Call the function "read_file" to open "task_overview.txt" and "user_overview.txt"
    read_user = read_file(file)
    read_tasks = read_file(file1)
    # length of user file and tasks file
    len_read_user = len(read_user)
    len_read_tasks = len(read_tasks)

    # Cycle "for" to read all task from file tasks
    for all_tasks in read_tasks:
        due_date_task = datetime.datetime.strptime(all_tasks[-2], "%d-%m-%Y")
        # "if" control to check task is not complete and the date is overdue
        if all_tasks[-1] == "No" and due_date_task < today:
            count_tasks_overdue += 1
        # "if" control to check task is not complete
        if all_tasks[-1] == "No":
            count_tasks_no_completed += 1
        else:
            count_tasks_completed += 1

    user_output = (f"The total number of users registered is : {len_read_user}\n")
    user_output += (f"The total number of tasks is : {len_read_tasks}\n")
    # Cycle "for" to read every line of user file
    for line_user in read_user:
        # Declare Variable
        count_user_task_assign = 0
        count_user_task_assign_complete = 0
        count_user_task_assign_no_complete = 0
        count_user_task_assign_overdue = 0
        # Cycle "for" to read every line of tasks file for every user
        for line_tasks in read_tasks:
            due_date_task = datetime.datetime.strptime(line_tasks[-2], "%d-%m-%Y")
            # "if" condition to check and count task assign, task complete, task not complete, and tasks overdue
            if line_user[0] == line_tasks[0]:
                count_user_task_assign += 1
            if line_user[0] == line_tasks[0] and line_tasks[-1] == "Yes":
                count_user_task_assign_complete += 1
            if line_user[0] == line_tasks[0] and line_tasks[-1] == "No":
                count_user_task_assign_no_complete += 1
            if line_user[0] == line_tasks[0] and line_tasks[-1] == "No" and due_date_task < today:
                count_user_task_assign_overdue += 1

        # Calculate the percentage of tasks assign to user and prepare the message to input in file "task_overview.txt"
        user_output += (f"\n*******************************************{line_user[0]}*******************************************\n").upper()
        user_output += (f"The total number of tasks is : {count_user_task_assign}\n")
        user_output += (f"The percentage of the total number of tasks is : {((count_user_task_assign * 100) / len_read_tasks):.2f}%\n")
        # "if" condition to check if "count_user_task_assign" is greater than 0
        if count_user_task_assign > 0:
            user_output += (f"The percentage of the tasks completed is : {((count_user_task_assign_complete * 100) / count_user_task_assign):.2f}%\n")
            user_output += (f"The percentage of the tasks must still be completed is : {((count_user_task_assign_no_complete * 100) / count_user_task_assign):.2f}%\n")
            user_output += (f"The percentage of the tasks have not yet been completed and are overdue is : {((count_user_task_assign_overdue * 100) / count_user_task_assign):.2f}%\n")
        else:
            user_output += (f"The percentage of the tasks completed is : 0.00%\n")
            user_output += (f"The percentage of the tasks must still be completed is : 0.00%\n")
            user_output += (f"The percentage of the tasks have not yet been completed and are overdue is : 0.00%\n")
        user_output += (f"******************************************************************************************\n").upper()

    # Calculate the percentage of tasks no complete and overdue, and prepare the message to input in file "task_overview.txt"
    percentage_tasks_no_completed = (count_tasks_no_completed * 100) / len_read_tasks
    percentage_tasks_overdue = (count_tasks_overdue * 100) / len_read_tasks

    task_output = (f"The total number of tasks is : {len_read_tasks}\n")
    task_output += (f"The total number of completed tasks is : {count_tasks_completed}\n")
    task_output += (f"The total number of uncompleted tasks is : {count_tasks_no_completed}\n")
    task_output += (f"The total number of tasks that haven’t been completed and that are overdue is : {count_tasks_overdue}\n")
    task_output += (f"The percentage of tasks that are incomplete is : {percentage_tasks_no_completed:.2f}%\n")
    task_output += (f"The percentage of tasks that are overdue is {percentage_tasks_overdue:.2f}%\n")

    # Call function write_to_file to write "task_overview.txt" and "user_overview.txt"
    write_to_file(file3, task_output, "w")
    write_to_file(file4, user_output, "w")

    if voice_menu == "a" or voice_menu == "vm":
        print("Well done, your report is update!")
    else:
        print("Well done, your report is create!")

# Function to check assign username
def check_assign_username():
    # Call function "user_file_to_dict"
    username_and_password = user_file_to_dict(file)
    print(f"This is the users inside \"{file}\".")
    # Cycle "for" to print username inside "user.txt"
    for count, user_to_txt in enumerate(username_and_password, 1):
        print(f"{count}.{user_to_txt} ", end=" ")
    print("\nMake sure to assign task of one of this users.\n")

    # Ask user to enter username of the person whom the task is assigned to
    name_to_assign = input("Please, enter a username of the person whom the task is assigned to : ")
    # Cycle "while": condition to exit "name_to_assign" is in "username_and_password" dict or the "name_to_assign" is not empty
    while not user_check(username_and_password, name_to_assign) or check_empty(name_to_assign):
        # Ask user to enter username of the person whom the task is assigned to
        # Print a message
        print(f"Sorry the user is not in the file {file} or username of the person whom the task is assigned is empty.")
        name_to_assign = input("Please, enter a username of the person whom the task is assigned to : ")

    return name_to_assign
# Function to Replace incorrect character from date
def replace_date_character(date_to_replace):
    # Replace incorrect character with "-"
    date_to_replace = date_to_replace.replace("/", "-").replace(" ", "-")

    return date_to_replace
# Function to check date is correct
def check_date(date_to_check):

    # Call function "replace_date_character"
    date_to_check = replace_date_character(date_to_check)
    # Split the date
    day, month, year = date_to_check.split("-")
    # Assign "this_year" to current year
    this_day = date.today().strftime("%d-%m-%Y") # today date
    this_year = date.today().strftime("%Y")
    date_to_check = f"{day}-{month}-{year}"

    # "if" to check is day, month and year is numeric
    if ((day.isnumeric()) and (month.isnumeric()) and (year.isnumeric())):
        # Cycle "while": condition to exit
        # day less than or equal to 31
        # day greater than "this_day"
        # month less then 12
        # day greater than or equal to "this_year"
        # date to check greater than today date
        while ((int(day) > 31) or (int(month) > 12) or int(year) < int(this_year) or (datetime.datetime.strptime(date_to_check, "%d-%m-%Y") < (datetime.datetime.strptime(this_day, "%d-%m-%Y")))):
            print("Sorry, uncorrect date. This is the format (dd-mm-yyyy)")
            print("\"day\" should be less than or equal to 31")
            print("\"month\" should be less than or equal to 12")
            print("\"year\" should be greater than or equal to this year")
            print("The date should be greater than or equal today date")
            date_to_check = input("Please, enter the due date of the task (dd-mm-yyyy) : ")
            date_to_check = replace_date_character(date_to_check)
            day, month, year = date_to_check.split("-")
    else:
        print("Sorry, uncorrect date. The date should be numeric (dd-mm-yyyy)")

    return  date_to_check
# Function to update the files
def update_file(dict):
    # Declare variable
    new_string_update = ""
    # Cycle "for" to read every key from dict
    for count, key_dict in enumerate(dict, 1):
        # Replace character to write into the file
        new_string_update += f"{str(dict[key_dict])}, ".replace("], ", "\n").replace("[\'", "").replace("'", "")
    # Call function "write_to_file"
    write_to_file(file1, new_string_update, "w")
# Function to read the files
def read_file(file):
    # Declare variable
    file_list = []

    # Open file "user.txt"
    with open(file, "r", encoding="utf-8-sig") as file_open:
        # Read every line from file
        file_read = file_open.readlines()
        # Cycle for to read file and append inside list "file_list"
        for file_read_row in file_read:
            file_read_split = file_read_row.strip("\n").split(", ")
            file_list.append(file_read_split)
    return file_list
# Function to create a view
def create_view(file_to_open, username=""):
    # Declare variable
    new_dict = {}
    task_counter = 0
    # Open file "task.txt"
    with open(file_to_open, "r") as task_file:
        # Cycle "for" to read file "task.txt"
        for num_task, task in enumerate(task_file, 1):
            # split and strip the line inside file
            strip_task = task.strip("\n").split(", ")
            # Output tasks
            output = f"______________________________{[num_task]}______________________________\n"
            output += f"Task : \t\t\t\t {strip_task[1]}\n"
            output += f"Assigned to : \t\t {strip_task[0]}\n"
            output += f"Date assigned : \t {strip_task[3]}\n"
            output += f"Due Date : \t\t\t {strip_task[4]}\n"
            output += f"Task Complete? : \t {strip_task[5]}\n"
            output += f"Task description : \n"
            output += f"{strip_task[2]}\n"
            output += "________________________________________________________________\n"
            output += "\n"
            # Create the dict "new_dict"
            new_dict[num_task] = strip_task
            # "if" condition to check username tasks and if menu is equal to "vm"
            if strip_task[0] == username and menu == "vm":
                # Count user login tasks and print out the task
                task_counter += 1
                print(output)
            # "if" condition to check menu is equal to "vm"
            elif menu == "va":
                # Count all tasks and print out the task
                task_counter += 1
                print(output)
        # "if" condition to check task_counter is equal to 0
        if task_counter == 0:
            print("Sorry, no task to show in this moment\n")

        # "if" condition to check menu is equal to "vm" and task_counter is greater than 0
        if menu == "vm" and task_counter > 0 :
            task_number = int(input("Please, enter a number the task you want change : "))
            # Print out the task choice
            print("\nThe task do you want to change is : ")
            print(f"Task number : {task_number}")
            print(f"{str(new_dict[task_number])}, ".replace("], ", "\n").replace("[\'", "").replace("'", ""))
            while True:
                # Ask a choice to user
                menu_edit = input('''Select one of the following options below :\n1 - Mark the task as complete\n2 - Edit the task\n-1 - Back to the main menu\n : ''')
                # "if" condition to check "menu_edit" is equal to 1 and mark task us complete
                if menu_edit == "1":
                    pass
                    # "if" condition to check task choice is complete
                    if(new_dict[task_number][-1] == "No"):
                        # Change task from no complete to complete
                        new_dict[task_number][-1] = "Yes"
                        # Call function "update_file"
                        update_file(new_dict)
                        generate_report("vm")
                        print("Wel done, your task now is complete!")
                    else:
                        print("Sorry, your task can not be change because is complete!")
                # "if" condition to check "menu_edit" is equal to 2 to edit the task selected
                elif menu_edit == "2":
                    pass
                    # "if" condition to check task is not complete
                    if new_dict[task_number][-1] == "No":
                        while True :
                            # Ask a choice to user
                            menu_change_date = input('''Select one of the following Options below :\n1 - Change username of the person to whom the task is assigned
2 - Change the due date\n0 - Back to the main menu\n : ''')
                            # "if" condition to check "menu_change_date" is equal to 1 and change username of the person to whom the task is assigned
                            if menu_change_date == "1":
                                pass
                                # Call function "check_assign_username"
                                change_assigned_name = check_assign_username()
                                # "if" condition to check "change_assigned_name" is equal to "user_log"
                                if change_assigned_name == user_log:
                                    print("Sorry, your username can not assign to this task.")
                                    change_assigned_name = input("Please, enter a username of the person whom the task is assigned to : ")
                                # Cycle "while" condition to exit "change_assigned_name" is not equal to "user_log"
                                while change_assigned_name == user_log:
                                    print("Sorry, your username can not assign to this task.")
                                    change_assigned_name = input("Please, enter a username of the person whom the task is assigned to : ")

                                # Change the username of the person whom the task is assigned
                                new_dict[task_number][0] = change_assigned_name
                                # Call function "update_file"
                                update_file(new_dict)
                                generate_report("vm")
                                print("Your username of the person whom the task is assigned is change!")

                            # "if" condition to check "menu_change_date" is equal to 2 and change the date to due
                            elif menu_change_date == "2":
                                pass
                                # Print out message and ask user date to change
                                print(f"Your date to change need to greater than \"{new_dict[task_number][-2]}\"")
                                # Ask user to enter the due date of the task
                                change_due_date_task = input("Please, enter the due date of the task (dd-mm-yyyy) : ")
                                # Call function "check_date"
                                change_due_date_task = check_date(change_due_date_task)

                                # "strptime" : Create a datetime object from "new_dict[task_number][-2]" and "change_due_date_task"
                                date_from_task = datetime.datetime.strptime(new_dict[task_number][-2] , "%d-%m-%Y")
                                change_due_date_task_strptime = datetime.datetime.strptime(change_due_date_task , "%d-%m-%Y")

                                # Cycle "while" : condition to exit "date_from_task" is greater than "change_due_date_task_strptime"
                                while change_due_date_task_strptime < date_from_task :
                                    # Print out message and ask user date to change
                                    print(f"Your date to change need to greater than \"{new_dict[task_number][-2]}\"")
                                    change_due_date_task = input("Please, enter the due date of the task (dd-mm-yyyy) : ")

                                    # Call function "check_date"
                                    change_due_date_task = check_date(change_due_date_task)
                                    # "strptime" : Create a datetime object from "new_dict[task_number][-2]" and "change_due_date_task"
                                    date_from_task = datetime.datetime.strptime(new_dict[task_number][-2] , "%d-%m-%Y")
                                    change_due_date_task_strptime = datetime.datetime.strptime(change_due_date_task , "%d-%m-%Y")
                                # Change the date in "new_dict[task_number][-2]" with "change_due_date_task"
                                new_dict[task_number][-2] = change_due_date_task
                                # Call function "update_file"
                                update_file(new_dict)
                                generate_report("vm")
                            elif menu_change_date == "0":
                                return
                            else:
                                print("Sorry, your choice is uncorrect!")
                    else :
                        print("Sorry, your task can not be change because is complete!")
                elif menu_edit == "-1" :
                    return
                else:
                    print("Sorry, your choice is uncorrect!")

# Function to check if password is match {comment ready}
def check_pass_match(passw, passw1):
    # "if" condition to check passwords match
    if passw != passw1:
        # Print out message
        print("Sorry, your password doesn't match.")
        pass_match = False
    else:
        pass_match = True

    return pass_match

# Function check if is inside the dictionary {comment ready}
def user_check(userpass_dict, username):
    # "if" condition to check username is into dict
    if(username in userpass_dict):
        check_user = True
    else:
        check_user = False

    return check_user

# Functione to check if the field is empty {comment ready}
def check_empty(str_to_check):
    # Strip string to check
    str_to_check = str_to_check.strip()
    # "if" condition to check string is not empty
    if str_to_check != "":
        empty_check = False
    else:
        empty_check = True

    return empty_check

# Function to write inside the file {comment ready}
def write_to_file(file_to_write, msg_to_write, mode = "a+"):
    # Open "file_to_write" and write inside
    with open(file_to_write, mode) as open_to_write:
        write_file = open_to_write.write(msg_to_write)

    return write_file

# Function to create a login dictionary (username : password) {comment ready}
def user_file_to_dict(file_to_open):
    # Declare variable
    userpass_dict = {}
    # Open "file_to_open" and read inside
    with open(file_to_open, "r", encoding="utf-8-sig") as open_file:
        for open_file_row in open_file:
            open_file_row_split = open_file_row.strip("\n").split(", ")
            # Assign username and password to dict
            userpass_dict[open_file_row_split[0]] = open_file_row_split[-1]

    return userpass_dict

# Function to login user {comment ready}
def login():
    # Ask user to enter him username and password
    user_name = input("Please, enter your username : ").lower()
    passwrd = input("Please, enter your password : ").lower()
    # "if" condition to check "user_name" is not inside "username_and_password" dict
    # Call function "user_check"
    if not user_check(username_and_password, user_name):
        # Cycle "while": condition to exit "user_name" is inside "username_and_password" dict
        # Call function "user_check"
        while not user_check(username_and_password, user_name):
            # Ask user to enter him username, password and print out message
            print("Sorry, your username or password is not correct!")
            user_name = input("Please, enter your username : ").lower()
            passwrd = input("Please, enter your password : ").lower()
        # "if" condition to check "username_and_password[user_name]" is not equal to "passwrd"
        # Call function "check_pass_match"
        if not check_pass_match(username_and_password[user_name], passwrd):
            # Ask user to enter him password
            passwrd = input(f"Please, enter password belonging to \"{user_name}\" : ")
            # Cycle "while": condition to exit "username_and_password[user_name]" is equal to "passwrd"
            # Call function "check_pass_match"
            while not check_pass_match(username_and_password[user_name], passwrd):
                # Ask user to enter him password
                passwrd = input(f"Please, enter password belonging to \"{user_name}\" : ")
            else:
                print(f"Welcome, {user_name}")
                temp_menu = True
        else:
            temp_menu = True
    # "if" condition to check "username_and_password[user_name]" is not equal to "passwrd"
    # Call function "check_pass_match"
    elif not check_pass_match(username_and_password[user_name], passwrd):
        # Ask user to enter him password
        passwrd = input(f"Please, enter password belonging to \"{user_name}\" : ")
        # Cycle "while": condition to exit "username_and_password[user_name]" is equal to "passwrd"
        # Call function "check_pass_match"
        while not check_pass_match(username_and_password[user_name], passwrd):
            # Ask user to enter him password
            passwrd = input(f"Please, enter password belonging to \"{user_name}\" : ")
        else:
            print(f"Welcome, {user_name}")
            temp_menu = True
    else:
        print(f"Welcome, {user_name}")
        temp_menu = True

    return temp_menu, user_name

# Function to register a user {comment ready}
def reg_user():
    # Ask the user to enter a username
    new_user_name = input("Please, enter a new username : ").lower()
    # Cycle "while" : condition to exit "new_user_name" is inside to "username_and_password" or "new_user_name" is not empty
    # Call function "user_check" and "check_empty"
    while user_check(username_and_password, new_user_name) or check_empty(new_user_name):
        # Ask the user to enter a username and print out message
        print("Sorry, the insert username is already used or your field is empty.")
        new_user_name = input("Please, enter a new username : ").lower()
    # Ask user to enter new password and confirm that
    new_passwrd = input("Please, enter a new password : ").lower()
    # Cycle "while" : condition to exit "new_passwrd" is not empty
    # Call function "check_empty"
    while check_empty(new_passwrd):
        # Ask the user to enter a "new_passwrd" and print out message
        print("Sorry, your password can not be empty.")
        new_passwrd = input("Please, enter a new password : ").lower()
    # Ask the user to enter a "new_passwrd_conf"
    new_passwrd_conf = input("Please, confirm password you insert : ").lower()
    # Cycle "while" : condition to exit "new_passwrd" is equal to "new_passwrd_conf"
    # Call function "check_pass_match"
    while not check_pass_match(new_passwrd, new_passwrd_conf):
        # Ask the user to enter a "new_passwrd_conf"
        new_passwrd_conf = input("Please, confirm password you insert : ").lower()
    # "if" condition to check new_user_name is not inside "username_and_password" dict and "new_passwrd" is equal to "new_passwrd_conf"
    if not user_check(username_and_password, new_user_name) and check_pass_match(new_passwrd, new_passwrd_conf):
        user_pass_msg = f"{new_user_name}, {new_passwrd}\n"
        # Call "write_to_file" function
        write_to_file(file, user_pass_msg)
        # Call "user_file_to_dict" function
        reg_user_pass = user_file_to_dict(file)
        print(f"\nWell done! Your username and password are insert in \"{file}\"")

# Function to add the tasks
def add_task():
    # Call function "check_assign_username"
    assigned_name = check_assign_username()

    # Ask user to enter title of a task
    title_task = input("Please, enter a title of a task : ")
    # Cycle "while" : condition to exit "title_task" is not empty
    while check_empty(title_task):
        # Ask user to enter title of a task and print out message
        print("Sorry, your title of a task can not be empty.")
        title_task = input("Please, enter a title of a task : ")
    # Ask user to enter description of a task
    description_task = input("Please, enter a description of the task : ")
    # Cycle "while" : condition to exit "description_task" is not empty
    while check_empty(description_task):
        # Ask user to enter description of a task and print out message
        print("Sorry, your description of the task can not be empty.")
        description_task = input("Please, enter a description of the task : ")

    # Ask user to enter the due date of the task
    due_date_task = input("Please, enter the due date of the task (dd-mm-yyyy) : ")
    # Cycle "while" : condition to exit "due_date_task" is not empty
    while check_empty(due_date_task):
        # Ask user to enter description of a task and print out message
        print("Sorry, your date to due of the task can not be empty.")
        due_date_task = input("Please, enter the due date of the task (dd-mm-yyyy) : ")
    # Call the function "check_date"
    due_date_task = check_date(due_date_task)
    # Create variable "current_date"
    current_date = today.strftime("%d-%m-%Y")
    complete_task = "No"

    # Write to file "task.txt"
    task_file_write = f"{assigned_name}, {title_task}, {description_task}, {current_date}, "
    task_file_write += f"{due_date_task}, {complete_task}\n"
    # Call "write_to_file" function
    write_to_file(file1, task_file_write)
    print("Well done! Your task is insert in task.txt")
    generate_report("a")

# Function to view all task
def view_all():
    # Call function "create_view"
    create_view(file1)

# Function to view the task of user login
def view_mine():
    # Call function "create_view"
    create_view(file1, user_log)

# Declare Variable
menu_temp = False
file = "user.txt"
file1 = "tasks.txt"
file3 = "task_overview.txt"
file4 = "user_overview.txt"

# Call function user_file_to_dict()
username_and_password = user_file_to_dict(file)

# Call function generate_report()
generate_report()
# "if" condition to check "task_overview.txt" and "user_overview.txt" is it create
#if not os.path.isfile(file3) and not os.path.isfile(file4) :
#    tasks_read_file = write_to_file(file3, "", "w")
#    user_read_file = write_to_file(file4, "", "w")

#====Login Section====
# Call function login()
menu_temp, user_log = login()

while menu_temp == True:
    # "if" condition to check "user_log" equal to "admin"
    if (user_log == "admin"):
        # New menu if you are "admin"
        # making sure that the user input is converted to lower case.
        menu = input('''Select one of the following options below :\nr - Register user\na - Adding a task\nva - View all tasks\nvm - View my task
gr - Generate report\nds - Display statistic\ne - Exit : ''').lower()
    else:
        # Menu if you are "user"
        menu = input('''Select one of the following options below :\na - Adding a task\nva - View all tasks\nvm - View my task\ne - Exit : ''').lower()

    if menu == 'r':
        pass
        # Call function reg_user()
        reg_user()
    elif menu == 'a':
        pass
        # Call function add_task()
        add_task()
    elif menu == 'va':
        pass
        # Call function view_all()
        view_all()
    elif menu == 'vm':
        pass
        # Call function view_mine()
        view_mine()

    elif menu == 'gr':
        pass
        # Call function generate_report()
        generate_report()

    elif menu == 'ds':
        pass
        # Call function display_statistic()
        display_statistic()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
