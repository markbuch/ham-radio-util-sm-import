# imports
import getpass

#  Function definitions


def add_ve():
    print("Adding VE")


def get_login_creds():
    print("Get Credentials")


def create_csv():
    print("creating csv")


#  Main Menu
current_choice = None
available_choices = {
    "1": "Add Signing VEs",
    "2": "Enter Login Credentials",
    "3": "Get Registered users and Create CSV",
}

# get password code to obscure password entry
# pwd = getpass.getpass(prompt='Password: ')
# print(f'Password: {pwd}')
# will use "0" as exit

while current_choice != "0":
    print("Please chose an option")
    print("-" * 25)
    print(f" DEBUG:: Available Choices: {available_choices}")
    if current_choice in available_choices:
        print(f"DEBUG:: Current Choice: {current_choice}")
        if current_choice == "1":
            print("DEBUG:: Current Choice is 1")
        elif current_choice == "2":


    else:
        print("Please chose from the menu")
        for key, value in available_choices.items():
            # print(key, value, sep=": ")
            print(f"{key}: {value}")
        print("0: To exit program")

    current_choice = input("> ")
