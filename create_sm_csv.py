# imports
import getpass

#  Function definitions


def add_ve():
    print("Adding VE")
    ve_list = []
    for i in range(3):
        ve = input(f"Please enter VE {i+1}'s callsign: ")
        choice = input(f"You entered {ve}. Is that correct? Y/N ")
        if choice.upper() == "Y":
            ve_list.append(ve.upper())
        else:
            ve = input(f"Please re-enter VE {i + 1}'s callsign: ")
            choice = input(f"You entered {ve}. Is that correct? Y/N ")
            if choice.upper() == "Y":
                ve_list.append(ve.upper())
            else:
                print("Exiting program.  Please try again.")

    print(f"list contains: {ve_list}")
    return None


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

    if current_choice in available_choices:
        print(f"DEBUG:: Current Choice: {current_choice}")
        if current_choice == "1":
            add_ve()
        elif current_choice == "2":
            get_login_creds()
        elif current_choice == "3":
            create_csv()
        else:
            print("DEBUG:: Reprint Menu.")

    else:
        print("Please chose an option")
        print("-" * 25)
        for key, value in available_choices.items():
            # print(key, value, sep=": ")
            print(f"{key}: {value}")
        print("0: To exit program")

    current_choice = input("> ")
