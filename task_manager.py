#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime #this was used to help validate the dated more effectively with less code

#A quick note that this program uses the delimeter "; " as in the short description of a task you can now use commas

#=====Function section============

def generate_report():
    
    tasks = [] # a list containing the number of tasks
    
    total_tasks = 0
    total_completed_tasks = 0
    total_incomplete_tasks = 0
    total_overdue_tasks = 0
    percentage_incomplete = 0
    percentage_overdue = 0
    
    try: 
        with open("task.txt", "r") as task_info:
            
            
            if task_info != "":
                
                for line in task_info:
                    
                    task = line.strip().split("; ")
                    
                    tasks.append(task)
                    
               
            else:
                print("\n***There are no tasks to genrate a report***\n")
                print("^^^Please add tasks^^^\n")
            
            for task in tasks:
                
                total_tasks += 1
                #checks if task is imcomplete irrespective of due date
                if task[5] == "No":
                    
                    total_incomplete_tasks += 1
                    
                elif task[5] == "Yes":
                    
                    total_completed_tasks += 1
                #checks if task is past the due date and incomplete
                if task[5] == "No" and datetime.date.fromisoformat(task[4]) < datetime.date.today():
                    
                    total_overdue_tasks += 1
                    
            percentage_incomplete = round((total_incomplete_tasks/total_tasks)*100,2)
            percentage_overdue = round((total_overdue_tasks/total_tasks)*100,2)
            
            with open("task_overview.txt","w") as task_overview:
                
                task_overview.write(f"{total_tasks}; {total_completed_tasks}; {total_incomplete_tasks}; {total_overdue_tasks}; {percentage_incomplete}; {percentage_overdue}")
             
            users = []
            
            with open("user.txt","r") as user_info:
               
                for line in user_info:
                    user = line.strip().split("; ")
                    users.append(user)
                    
                
            
            with open("user_overview.txt","w") as user_overview: 
                for user in users:
                    
                    user_total_tasks = 0
                    percentage_tasks_assigned = 0
                    percentage_user_completed = 0
                    percentage_user_incomplete = 0
                    percentage_user_overdue = 0
                    
                    num_completed = 0
                    num_incomplete = 0
                    num_overdue = 0
                    
                    for task in tasks:
                        
                        if user[0] == task[0]:
                            
                            user_total_tasks += 1
                            
                            if task[5] == "No":
                                
                                num_incomplete += 1
                                
                            elif task[5] == "Yes":
                                
                                num_completed += 1
                            #checks if task is past the due date and incomplete
                            if task[5] == "No" and datetime.date.fromisoformat(task[4]) < datetime.date.today():
                                
                                num_overdue += 1
                                
                    percentage_tasks_assigned = round((user_total_tasks/total_tasks)*100,2)
                    percentage_user_completed = round((num_completed/user_total_tasks)*100,2)
                    percentage_user_incomplete = round((num_incomplete/user_total_tasks)*100,2)
                    percentage_user_overdue = round((num_overdue/user_total_tasks)*100,2)
                    
                    user_overview.write(f"{user[0]}; {user_total_tasks}; {percentage_tasks_assigned}; {percentage_user_completed}; {percentage_user_incomplete}; {percentage_user_overdue}\n")
    
        print("\n^^^Report successfully generated^^^\n")
    
    except   (FileNotFoundError, IndexError) :
        
        print("\n***There are no tasks to generate a report***\n")
        print("^^^Please add tasks^^^\n")
        
        
                

def write_to_file(file,list1,list2):

    with open(file,"w") as task_file:
         
         for i in range(len(list2)):
             
                 task_file.writelines(list2[i][0] + "; " + list2[i][1] + "; " + list2[i][2] + "; " + list2[i][3] + "; " + list2[i][4] + "; " + list2[i][5] + "\n")
         
         
         for i in range(len(list1)):
             
                 task_file.writelines(list1[i][0] + "; " + list1[i][1] + "; " + list1[i][2] + "; " + list1[i][3] + "; " + list1[i][4] + "; " + list1[i][5] + "\n")




#create a funtion that takes the user dictionary containing all usernames and passwords and add a new user to it and the text file.
'''This code block will add a new user to the user.txt file
- You can use the following steps:
    - Request input of a new username
    - Request input of a new password
    - Request input of password confirmation.
    - Check if the new password and confirmed password are the same
    - If they are the same, add them to the user.txt file,
      otherwise present a relevant message'''
def reg_user(user_info_dic):
    while True:
        
        #create variables to store new username, new password, and confirm password
        new_user = input("New Username: ")
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        
        if new_user not in user_info_dic: # checks if username already exists
            
            if new_password not in list(user_info_dic.values()): # checks if password already exists
                
                if new_password == confirm_password: # validate whether passwords match
                    
                    with open("user.txt","a") as user_info:
                    
                        user_info.write(new_user + "; " + new_password + "\n")
                        print("\nSuccessfully registered new user!") #indicates to user that function was successful
                        
                    break
                
                else:
                    print("Passwords do not match try again.\n")
            else:
                print("Password already exists. Please try again\n")
                
        else:
             print("Username already exists. Please try again\n")

#create a funtion that takes the user dictionary containing all usernames and passwords and add a new task to the text file.
'''This code block will allow a user to add a new task to task.txt file
- You can use these steps:
    - Prompt a user for the following: 
        - the username of the person whom the task is assigned to,
        - the title of the task,
        - the description of the task, and 
        - the due date of the task.
    - Then, get the current date.
    - Add the data to the file task.txt
    - Remember to include 'No' to indicate that the task is not complete.'''
def add_task(user_info_dic):
    while True:
        #create varaible to capture who the task is assigned to
        task_assigned_user = input("\nPlease enter the username of the employee you want to assign a task to\nType here: ")
        
        if task_assigned_user in list(user_info_dic.keys()): # validates whether user exists or not
            
            #create variables to hold title of task, task description and the dates relevant to task 
            
            task_title = input("\nWhat is the title of the task?\nType here:  ")
            task_description = input("\nWrite a short description of the task.\nType here: ")
            
            while True: #this block will validate the dates correctly and automatically assign the current date
                
                try:
                    
                    cur_date = datetime.date.today()
                    print(f"\nToday's date is {cur_date}")
                    
                    date_before = list(map(int, input("\nEnter the due date of the task in yyyy,m,d(e.g.2024,2,3 will represent 3 March 2024 )format.\nType here: ").split(",")))
                    due_date = datetime.date(date_before[0],date_before[1],date_before[2])
                    
                    
                    if cur_date <= due_date :
                        
                        break
                    
                    else:
                        print("\n***Inavild due date entered***\n")
                        
                except:
                    print("\n***Invalid entry entered***\n")
                
                
            task_complete = "No"
            try: 
                with open("task.txt","a") as task_file: #opens file in append mode
                    
                    #writes task to the file
                    task_file.write(task_assigned_user + "; " + task_title + "; " + task_description + "; " + str(cur_date) + "; " + str(due_date) + "; " + task_complete + "\n")
            
            except  FileNotFoundError:
                with open("task.txt","w") as task_file: #opens file in append mode
                    
                    #writes task to the file
                    task_file.write(task_assigned_user + "; " + task_title + "; " + task_description + "; " + str(cur_date) + "; " + str(due_date) + "; " + task_complete + "\n")
            
            
            print(f"\nSuccessfully added a task for {task_assigned_user}\n")
            
            break
        
        else:
            print("OOPS! you entered an invalid employee username.")

#create a funtion that takes the user dictionary containing all usernames and passwords to view all tasks from the text file.
'''This code block will read the task from task.txt file and
 print to the console in the format of Output 2 presented in the PDF
 You can do it in this way:
    - Read a line from the file.
    - Split that line where there is comma and space.
    - Then print the results in the format shown in the Output 2 in the PDF
    - It is much easier to read a file using a for loop.'''
def view_all(user_info_dic):
    # first open the file with the tasks
   try: 
       with open("task.txt","r") as task_file: # opened in read mode
       
           if task_file != "":
               
               print("-"*75)
               for line in task_file:
                   task = line.strip().split("; ") # stores one task at a time with all its details in a list
                   
                   # display task
                   
                   if task[0] != "":
                       spacing = "\t"*4 #Easier to format output sapcing from heading in each line
                       
                      
                       
                       print(f"\nTask:{spacing}\t\t{task[1]}")
                       print(f"Assigned to:{spacing}{task[0]}")
                       print(f"Date assigned:{spacing}{task[3]}")
                       print(f"Due date:{spacing}\t{task[4]}")
                       print(f"Task complete?{spacing}{task[5]}")
                       print(f"Task description:\n {task[2].capitalize()}")
                       print("\n"+"-"*75)
             
           else:
                    print("\n***There are no tasks to display***\n")
                    print("^^^Please add tasks^^^\n")
                  
   except FileNotFoundError:
       print("\n***There are no tasks to display***\n")
       print("^^^Please add tasks^^^\n")

#create a funtion that takes the username as a parameter to view a single users tasks from the text file.
'''This code block will read the task from task.txt file and
 print to the console in the format of Output 2 presented in the PDF
 You can do it in this way:
    - Read a line from the file
    - Split the line where there is comma and space.
    - Check if the username of the person logged in is the same as the 
      username you have read from the file.
    - If they are the same you print the task in the format of Output 2
      shown in the PDF '''
def view_mine(user_info_dic,username):
    # open and process file
    try:

        with open("task.txt","r") as task_file: # opened in read mode to read.
            
            error_message = ""
            list_tasks_user = [] #this will hold all the relevant tasks for user
            list_tasks = []
            
            if task_file != "":
            
                for line in task_file:
                    task = line.strip().split("; ") # stores one task at a time with all its details in a list
                    
                    
                    
                    if task[0] == username : #checks for tasks only associated with the user logged in
                        
                        list_tasks_user.append(task)    
                    
                    elif task[0] != "":
                         
                        list_tasks.append(task) #adds remaining tasks to list so all tasks are present after writing to the file again after editing
               
            else:
                print("\n***There are no tasks to display***\n")
                print("^^^Please add tasks^^^\n")
        
        while True:   
            
            task_counter = 0 #this will be used to count tasks and display a key number associated with a task
            
            for item in list_tasks_user:
                
                # display task
                
                spacing = "\t"*4 #Easier to format output sapcing from heading in each line
                
                print("-"*75)
                print(f"\nTask {task_counter+1}:{spacing}\t\t{item[1]}")
                print(f"Assigned to:{spacing}{item[0]}")
                print(f"Date assigned:{spacing}{item[3]}")
                print(f"Due date:{spacing}\t{item[4]}")
                print(f"Task complete?{spacing}{item[5]}")
                print(f"Task description:\n {item[2].capitalize()}")
                print("\n"+"-"*75)
                task_counter += 1
                
            try:     
                print(error_message)
                selected_task = int(input('''Please select a task to edit or exit to main menu
to select a task, type in the task number
to exit back to main menu please enter a negative number or zero
Type here: ''')) #this just stores the task number
        
                if 0 < selected_task < len(list_tasks_user)+1 :
                    
                    error_message = ""
                    curr_task = list_tasks_user[selected_task-1] # this holds the selected task for editing
                    
                    
                    while True: 
                        print(f"\nYou have selected task {selected_task}: {curr_task[1]}")
                        edit_or_mark_complete = input('''\nPlease enter whether you would like to edit the task or mark as complete
either type "edit" or "mark complete" to select action, enter "exit" to leave this page
Type here: ''').lower()
                        
                        if edit_or_mark_complete == "edit":
                            
                            if curr_task[5] == "No":
                                
                                while True:
                                    what_to_edit = input("\nPlease indicate what you would like to edit\nType either 'username' or 'due date'\nType here: ").lower()
                                    
                                    if what_to_edit == "username":
                                        while True:
                                            updated_user = input("\nPlease enter the new user's username you would like to assign the task to\nType here: ")
                                            
                                            if updated_user in user_info_dic :
                                               
                                                curr_task[0] = updated_user
                                                write_to_file("task.txt", list_tasks_user , list_tasks)
                                               
                                                break
                                            else:
                                                print("\n***User does not exist***\n")
                                        break
                                    
                                    elif what_to_edit == "due date":
                                        while True:
                                            try:
                                                today_date = datetime.date.today()
                                                print(f"\nToday's date is {today_date}")
                                                print(f"\nDate assigned is {curr_task[3]}")
                                                date_before = list(map(int, input("\nEnter the due date of the task in yyyy,m,d(e.g.2024,2,3 will represent 3 March 2024 )format.\nType here: ").split(",")))
                                                updated_date = datetime.date(date_before[0],date_before[1],date_before[2])
                                                if datetime.date.fromisoformat(curr_task[3]) <= updated_date and today_date <= updated_date :
                                                    
                                                    curr_task[4] = str(updated_date)
                                                    write_to_file("task.txt", list_tasks_user , list_tasks)
                                                    
                                                    break
                                                else:
                                                    print("\n***Invalid date was entered***\n")
                                            except:
                                                print("\n***Invalid input***\n")
                                                
                                        break
                                    
                                    else:
                                        print("\n***Invalid input***\n")
                                
                            else:
                                
                                error_message = "\n***This task has already been completed and cannot be edited.***\n" #prints feedback to user
                                
                            break
                        
                        elif edit_or_mark_complete == "mark complete":
                            curr_task[5] = "Yes"
                            # overwrites the file with updated tasks
                            write_to_file("task.txt", list_tasks_user , list_tasks)
                            break
                        
                        elif edit_or_mark_complete == "exit":
                            break
                       
                        else:
                            print("\n***Invalid option selected***\n")
                            
                        
                
                
                elif selected_task <= 0:
                    break
                    return
                
                
                else:
                    error_message = "\n***Task does not exist***\n"
            except ValueError  :
                error_message = "\n***Invalid input please enter a number to proceed***\n"
            
    except FileNotFoundError:
        print("\n***There are no tasks to display***\n")         
        print("^^^Please add tasks^^^\n")

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''


# open user.txt file and get information from it
# create a boolean value valid to hold information about validated username and password

                    
 # use a dictionary to avoid having two lists
user_info_dic = {} # a dictionary to store a username as a key with a matching password associated with it
valid = False
while True:
    try:
        with open("user.txt","r") as user_info:
            
            for line in user_info:
                
                line = line.strip() # just in case any \n characters are included
                line = line.split("; ") # the space after the comma is to prevent the space being part of the password
                
                user_info_dic[line[0]] = user_info_dic.get(line[0],line[1]) # adds username with corresponding password to dictionary
            break
    except FileNotFoundError :
        with open("user.txt","w") as user_info:
            
            user_info.write("admin; adm1n\n") # a default username and password

print("*"*7+" Welcome! Please login to continue "+"*"*7)

while valid == False:
    
    # get the login details from user, tand validate based on what is contained in the user.txt file
    username = input("Username: ")
    password = input("Password: ")
    print()
    
    # add conditional statements to validate user input
    
    if username in user_info_dic:
        if password == user_info_dic[username]:   #password will only be checked if username is valid first
            valid = True
            
        else:
            print("Invalid password! enter details again")
    
    else:
        print("Invalid username! Please enter details again")
#===== Menu section =====    
if valid : 
    
        while True:
            # the menu will only open if valid username and password is entered
            # Present the menu to the user and 
            # make sure that the user input is converted to lower case.
            
            # create a menu string to display different menus for different users
            
            if username == "admin":
                
                menu_string = "\n"+"*"*80 +"\n"+'''Select one of the following options:
                r - register a user
                ds - display statistics
                a - add task
                va - view all tasks
                gr - generate report
                vm - view my tasks
                e - exit\n'''
            
            else:
                menu_string = "\n"+"*"*80 +"\n"+'''Select one of the following options:
                a - add task
                va - view all tasks
                vm - view my tasks
                e - exit\n'''
            
                
            menu = input(menu_string +"*"*80+
            "\n\nType here: ").lower()
            
            if menu == 'r' and username == "admin":
               
                #print a statement indicating to the user which page they are on
                print()
                print("*"*10+" Register a new user "+"*"*10)
                
                #calling reg_user funtion
                reg_user(user_info_dic)
                
                #this makes sure the new user will be recognised in order to add a task
                with open("user.txt","r") as user_info:
                    
                    for line in user_info:
                        
                        line = line.strip() # just in case any \n characters are included
                        line = line.split("; ") # the space after the comma is to prevent the space being part of the password
                        
                        user_info_dic[line[0]] = user_info_dic.get(line[0],line[1]) # adds username with corresponding password to dictionary
                   
                            
            
            elif menu == 'a':
                
                #print a statement indicating to the user which page they are on
                print("\n"+"*"*10+" Add a task "+"*"*10+"\n")
                
                #print a list of the employees so mistakes are made when entering the username
                
                view_employee_list = input("Would you like to view the list of employees before assigning the task?\nType Yes or No: ").capitalize()
                
                if view_employee_list == "Yes":
                    
                    print("Employee list:")
                    
                    for employee in list(user_info_dic.keys()):
                        print(employee)
                else:
                    print("\n***Okay**\n")
                #calling the add task funtion
                add_task(user_info_dic)
               
            elif menu == 'va':
                
                #calling view_all function
                view_all(user_info_dic)
                
                 
            
            elif menu == 'vm':
                pass
                
                print() # output neatness
                
                view_mine(user_info_dic, username)
            
            elif menu == 'ds' and username == "admin":
                '''This block will provide statitics to the admin user only.'''
                # create variables to store stats of tasks and stats of users

                try:
                    with open("task_overview.txt","r") as task_overview :
                        
                        for stat in task_overview:
                            task_stats = stat.strip().split("; ")
                            
                        
                        
                           
                    print("\n" + "*"*10 + " Overall Task Statistics " + "*"*10)
                    print(f'''Total tasks: {task_stats[0]}
Completed tasks: {task_stats[1]}
Incomplete tasks: {task_stats[2]}
Overdue tasks: {task_stats[3]}
Percentage of Incomplete tasks: {task_stats[4]}%
Percentage of Overdue tasks: {task_stats[5]}%\n''')    
                    print("*"*45)                    
                    print("-"*45)
                    print("*"*10 + " Overall User satistics " + "*"*10)           
                    with open("user_overview.txt","r") as user_overview:
                        
                        user_stat = []
                        
                        for user in user_overview:
                            
                            user_stat = user.strip().split("; ")
                            print(f'''User: {user_stat[0]}
Total tasks assigned to user: {user_stat[1]}
Percentage of tasks assigned to user: {user_stat[2]}%
Percentage of tasks user has completed: {user_stat[3]}%
Percentage of tasks user has not completed: {user_stat[4]}% 
Percentage of tasks that are overdue for the user: {user_stat[5]}%                  
''')
                    
                    print("*"*45)   
                                
                except FileNotFoundError :
                    
                    print("\n***Please generate report first***\n")
                           

                        
            elif menu == 'gr'   and username == "admin":
                
                generate_report()
                
                
            elif menu == 'e':
                print("\n" + "<"*10 + ' Goodbye!!! ' + ">"*10)
                break
            
            else:
                print("\nInvalid option!")
    

        
        
        
        
        