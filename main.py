import sqlite_connection, uuid
from master import MasterPassword
# create a auth folder with keys and db?
print("Welcome to FIRSTPASS")

master = MasterPassword()
mstr_psswd = input("Enter the master password\nIf you don't know, press enter\n> ")
access = False
while access != True:
    check = master.load(mstr_psswd)
    if check == None:
        mstr_psswd = input("Enter a master password\nNote* you must remember this password to access all other passwords\n> ")
        master.create_master_psswd(mstr_psswd)
    elif check == False:
        print("The master password was incorrect")
        mstr_psswd = input("Enter the master password\n> ")
    else:
        access = True

sqlite_connection.create_table()
def select(): # consider using a while loop instead - recursion limit is 1000, and loop may be faster
    print("Select one")
    print(f"1) View passwords\n2) New password\n3) Edit Password\n4) Delete password\n5) Quit")

    option = input("> ")
    while option not in ["1", "2", "3", "4", "5"]:
        print(f"1) View passwords\n2) New password\n3) Edit Password\n4) Delete password\n5) Quit")
        option = input("> ")
    return option
    """
    if option not in ["1", "2", "3", "4"]:
        print("Invalid option")
        return select()
    else:
        return option
    """
    
x = 0
while x == 0:
    selection = select()
    
    if selection == "1":
        sqlite_connection.view()
    elif selection == "2":
        new_id = uuid.uuid4().__str__()
        site = input("What website is this for? ")
        username = input("What is the username of this site? ")
        password = input ("What is the password of this site? ")
        print("New password inserted with the ID " + new_id[:4] + "\n-----")

        sqlite_connection.insert(site, username, password, new_id[:4])
        # selection = select() restart the program so it doesnt end
    elif selection == "3":
        # get id
        id = input("What is the ID of the password you want to edit?")
        password = sqlite_connection.get_passwd(id)
        while password == None:
            print("Invalid ID")
            id = input("What is the ID of the password you want to edit?")
            password = sqlite_connection.get_passwd(id)

        x = 1
        change = input("What do you want to change?\n1) Username\n2) Password\n> ")
        while change not in ["1", "2"]:
            change = input("What do you want to change?\n1) Username\n2) Password\n> ")
        else:
            pass
            print("point a")
            x = 0 # repeats selection process

    elif selection == "4": # delete passwords
        # get id
        id = input("What is the ID of the password you want to delete?")
        password = sqlite_connection.get_passwd(id)
        while password == None:
            print("Invalid ID")
            id = input("What is the ID of the password you want to delete?")
            password = sqlite_connection.get_passwd(id)
            #selection = select() # err
        #else:
        print("Deleting password with ID " + id)
        sqlite_connection.delete(id)
    
    elif selection == "5":
        exit()