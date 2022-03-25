# imports
import getpass

#  Function definitions


def print_menu(menu_choices):
    print("Please choose a Menu option")
    print("-" * 25)
    for key, value in menu_choices.items():
        # print(key, value, sep=": ")
        print(f"{key}: {value}")
    print("0: To exit program")


def get_ves():
    print("Adding VEs")
    ve_list = []
    for i in range(3):
        ve = input(f"Please enter VE {i+1}'s callsign > ")
        choice = input(f"You entered {ve.upper()}. Is that correct? Y/N, Press C to Cancel > ")
        if choice.upper() == "Y":
            ve_list.append(ve.upper())
        elif choice.upper() == "C":
            print("Exiting to Main Menu ")
            break
        else:
            ve = input(f"Please re-enter VE {i + 1}'s callsign: ")
            choice = input(f"You entered {ve.upper()}. Is that correct? Y/N, Press C to Cancel > ")
            if choice.upper() == "Y":
                ve_list.append(ve.upper())
            elif choice.upper() == "C":
                print("Exiting to Main Menu ")
                break
            else:
                print("Exiting to Main Menu")
                break

    #  print(f"list contains: {ve_list}")
    return tuple(ve_list)


def get_mail_server():
    print("Get Mail Server address")


def get_login_creds():
    # get password code to obscure password entry
    # pwd = getpass.getpass(prompt='Password: ')
    # print(f'Password: {pwd}')
    email_account = input("Enter the email address to login with > ")

    print("Get Credentials")


def create_csv():
    print("create csv")


#  Main Menu
current_choice = None

# will use "0" as exit
available_choices = {
    "1": "Add Signing VEs",
    "2": "Enter Mail Server",
    "3": "Enter Login Credentials",
    "4": "Get Registered users and Create CSV",
}

while current_choice != "0":

    if current_choice in available_choices:
        print(f"DEBUG:: Current Choice: {current_choice}")
        if current_choice == "1":
            ves = get_ves()
            if len(ves) == 3:
                print(f"Tuple of VEs: {ves}")
            else:
                print_menu(available_choices)
        elif current_choice == "2":
            get_mail_server()
        elif current_choice == "3":
            get_login_creds()
        elif current_choice == "4":
            create_csv()
        else:
            print("DEBUG:: Reprint Menu.")

    else:
        # Display the menu
        print_menu(available_choices)
    current_choice = input("> ")
