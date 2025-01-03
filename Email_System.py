import csv
import re
import pathlib

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
    def check_email_existence(email):
        for user in Data.lst_users:
            if user.email == email:
                return True

    @staticmethod
    def print_password_rules():
        password_rules = '''
                     <password rules>:
                     one upper letter
                     one lower letter 
                     one special character
                     one number
                     Maximum length: 10'''
        print(password_rules)

    @staticmethod
    def isvalid_password(password):
        pattern = r"^(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{1,10}$"
        return re.match(password,pattern)

    @staticmethod
    def get_password_by_email(email):
        for user in Data.lst_users:
           if user.email == email:
               return user.password

class Data:
    lst_users = []

    @classmethod
    def add(cls, user):
        Data.lst_users.append(user)
    # working with csv file

    @staticmethod
    def file_is_exist(file_path):
        file_path = pathlib.Path(file_path)
        return file_path.exists()


    @staticmethod
    def read_file(file=r"E:\Documents\PythonProject\users.csv"):
        file_lst_users = []
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["Name"]
                email = row["Email"]
                password = row["Password"]
                Users(name, email, password, file=True)
                print(row)
            return file_lst_users

    @classmethod
    def import_file_users(cls,file_lst_users):
        for user in file_lst_users:
          cls.lst_users.append(user)

    @classmethod
    def store_data_in(cls, file=r"E:\Documents\PythonProject\users.csv"):
        with open(file, "a", newline="") as f :
            fieldnames = ["Name", "Email", "Password"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for user in Data.lst_users:
                user_info = {}
                user_info["Name"] = user.name
                user_info["Email"] = user.email
                user_info["Password"] = user.password
                writer.writerow(user_info)

if __name__ == "__main__":

    #  chhecking existence
    file = r"E:\Documents\PythonProject\users.csv"
    file_is_exist = Data.file_is_exist(file)
    if not file_is_exist:
        print("file not found")

    # read data & import
    file_users = Data.read_file(file)
    Data.import_file_users(file_users)


    while True:
        message = '''
        Bank system:
        Enter your choice number:
        1- Register
        2- Log in
        3- end the program'''
        print(message)
        choice = input(">>")

        for user in Data.lst_users:
            print(user)
        # registration
        if choice == "1":
           name = input("Enter your name: ")
           # get email
           while True:
               inp_email = input("Enter your email (Press 0 to cancel): ")
               if inp_email == "0": break
               # check email validation
               isvalid = Users.email_validation(inp_email)
               if not isvalid:
                   print("Invalid email")
                   continue
               else:
                 is_exist = Users.check_email_existence(inp_email)
                 if is_exist:
                   print("This email is already exist")
                   continue

           # got password
               while True :
                   Users.print_password_rules()
                   inp_password = input("Enter password (press 0 to cancel): ")
                   if inp_password == "0": break
                   # if isvalid_password(inp_password):
                   Users(name, inp_email, inp_password)
                   print("successfully registration !")
                   break
               break
                   # else:
                   #     print("Invalid password")
        # log in
        elif choice == "2":
          # get email
            while True:
              inp_email = input("Enter your registered email (Press 0 to cancel): ")
              if inp_email == "0": break
              # check email existence
              is_exist = Users.check_email_existence(inp_email)
              if not is_exist :
                  print("Email doesn't exist")
                  continue
        # got password
              while True :
                inp_password = input("Enter your password (Press 0 to cancel): ")
                if inp_password == 0 : break
            #      check password correctness
                password = Users.get_password_by_email(inp_email)
                if inp_password == password:
                    print("log in successfully")
                    break
            break

        elif choice == "3":
            print("Thank you") # flushing feature
            # saving data in a file
            Data.store_data_in(file)
            break

        else:
            print("invalid input")
