# imports
import getpass

#  Function definitions


def print_menu(menu_choices):
    #  print the main menu
    print("Please choose a Menu option")
    print("-" * 27)
    for key, value in menu_choices.items():
        # print(key, value, sep=": ")
        print(f"{key}: {value}")
    print("0: To exit program")


def get_certifying_ves():
    #  Get signing VEs from user
    print("DEBUG:: Adding VEs")
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

    #  return list of VEs as a Tuple, since list of VEs need to maintain order.
    return tuple(ve_list)


def get_mail_server():
    print("DEBUG:: Get Mail Server address")
    mail_server = input("Enter the url for the mail server >")
    return mail_server.strip()


def get_login_creds():
    print("DEBUG:: Get Credentials")
    # Get mail user and password from input
    # pwd = getpass.getpass(prompt='Password: ')
    # print(f'Password: {pwd}')
    email_user = input("Enter the email address to login with > ")
    print(f'DEBUG:: You entered {email_user}.')
    pwd = getpass.getpass(prompt='Enter Password > ')
    print(f'Password: {pwd}')
    return email_user.strip(), pwd.strip()


def login_to_mail_server():
    print(f'DEBUG:: Enter login to mail server')


def get_email_registrations():
    print('DEBUG:: getting emails')


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
            ves = get_certifying_ves()
            if len(ves) == 3:
                print(f"Tuple of VEs: {ves}")
            else:
                # print_menu(available_choices)
                continue
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
