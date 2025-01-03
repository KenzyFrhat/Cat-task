import csv
import re


class Users:

    def __init__(self, name, email, password, file=False):
        self.name = name
        self.email = email
        self.password = password
        if not file:
          Data.add(self)

    def __repr__(self):
        return f"name={self.name}, email={self.email}, password={self.password}"

    #  check email validation
    @staticmethod
    def email_validation(email):
        pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
        return re.match(pattern,email)

    @staticmethod
    def check_password_complexity(password):
        pattern = r"^(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{1,10}$"
        return re.match(password,pattern)

    @staticmethod
    def print_password_rules():
        password_rules = '''
                  <password rules>:
                  one upper lette
                  one lower letter 
                  one special character
                  one number
                  Maximum length: 10'''
        print(password_rules)


    def register(self):
        ...
    def logging_in(self):
        ...


class Data:
    lst_users = []

    @classmethod
    def add(cls, user):
        Data.lst_users.append(user)


    # working with csv file

    @staticmethod
    def read_file(file=r"E:\Documents\PythonProject\users.csv"):
        file_lst_users = []
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["Name"]
                email = row["Email"]
                password = row["Password"]
                user = Users(name, email, password, file=True)
            return file_lst_users

    @classmethod
    def add_file_users(cls,file_lst_users):
        for user in file_lst_users:
          cls.lst_users.append(user)

if __name__ == "__main__":
    while True:
        message = '''
        Bank system: 
        Enter your choice number:
        1- Register
        2- Log in
        3- end the program'''
        print(message)
        choice = input(">>")


        # registration
        if choice == "1":
           #  get name
           name = input("Enter your name: ")

           # get email
           while True:
               email = input("Enter your email: ")
               if Users.email_validation(email):
                 break
               else:
                   print("Invalid email")

           #  get password
           while True :
               Users.print_password_rules()
               inp_password = input("Enter password: ")
               break
               # if Users.check_password_complexity(inp_password):
               #     break
               # else:
               #     print("Invalid password")
           Users(name, email, inp_password)
           print("successfully registration !")
           continue





        # log in
        elif choice == "2":
            ...

        elif choice == "3":
            print("Thank you") # flushing feature
            break
        else:
            print("invalid input")







