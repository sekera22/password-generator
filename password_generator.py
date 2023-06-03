import sqlite3
import random
import string

def main():
    print("1) Add e-mail and password (1)")
    print("2) View registered (2)")
    print("3) Delete record (3)")
    print("4) Exit (4)") 
    db_process()
    
#To create a database and insert e-mail and password datas into the database.   
def db_process():
    connection = sqlite3.connect("password_generator.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS PASSWORD(
    email text,
    password text
    ) """)
    while True:
        selection = input("Choose a process:")
        
        #Insert e-mail and password to the database. 
        if selection == "1":
            email = email_input()
            password = password_generator()
            data = (email, password)
            add_commend = """INSERT INTO PASSWORD VALUES {}"""
            cursor.execute(add_commend.format(data))
            print("Generated password:", password)

        #View e-mails.    
        elif selection == "2":
            cursor.execute("""SELECT email from PASSWORD """)
            list_all = cursor.fetchall()
            if len(list_all) == 0:
                print("Such an empty database.")
            else:
                for char in list_all:
                    print(char[0])
        #Delete record.
        elif selection == "3":
            cursor.execute("""SELECT email from PASSWORD """)
            list_all = cursor.fetchall()
            if len(list_all) == 0:
                print("There is no any record in database.")
            else:
                for char in list_all:
                    print(char[0])
                del_element = input("Enter an e-mail from the list to delete: ")
                query = """DELETE FROM PASSWORD WHERE email = ?"""
                cursor.execute(query, (del_element,))

        #Exit
        elif selection == "4":
            print("Thanks for using password generator.")
            connection.commit()
            connection.close
            break
    

#Generate a random 12 characters password.
def password_generator():
    password = ""
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    nums = string.digits
    for _ in range(4):
        password += random.choice(lowercase_letters)
        password += random.choice(uppercase_letters)
        password += random.choice(nums)
    chars = list(password)
    random.shuffle(chars)
    password = "".join(chars)
    return password

#To get e-mail address input from the user.
def email_input():
    return input("Enter your e-mail address that you want to connect with a random password: ") 
    
if __name__ == "__main__":
    main()


