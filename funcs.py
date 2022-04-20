# imports
import getpass


def print_menu(menu_choices):
    #  print the main menu
    print("Please choose a Menu option")
    print("-" * 27)
    for key, value in menu_choices.items():
        # print(key, value, sep=": ")
        print(f"{key}: {value}")
    print("0: To exit program")


def get_ve(ve_num):
    # Give 2 chances to enter valid VE, otherwise, exit to main menu

    for i in range(2):
        ve = input(f"Enter VE #{ve_num}'s call sign > ")
        if len(ve) <= 3 or len(ve) > 6:
            print("An INVALID call sign was entered.")
            if i == 1:
                return "cancel"
            else:
                continue

        choice = input(f"You entered {ve.upper()}. Is that correct? Y/N, or C to Cancel > ")
        if choice.upper() == "N":
            if i == 1:
                return "cancel"
            continue
        elif choice.upper() == "C":
            print("Exiting program...")
            return "cancel"
        else:
            return ve.upper()


def get_certifying_ves():
    #  Get signing VEs from user
    print("DEBUG:: Getting VEs")
    ve_list = []

    for i in range(3):
        print(f"Getting VE #{i+1}")
        ve = get_ve(i+1)
        if ve == "cancel" or ve == "None":
            return "None"

        ve_list.append(ve)
    #  return list of VEs as a Tuple, since list of VEs need to maintain order.
    return tuple(ve_list)


def get_mail_server():
    mail_server = input("Enter the mail server URL > ")
    choice = input(f"You entered {mail_server}. Is that correct? Y/N.")
    if choice.upper() == "N":
        print("Exiting to Main Menu.  Please try again")
        return "Cancel"

    return mail_server.strip()


def get_login_creds():
    email_user = input("Enter the email address to login with > ")
    pwd = getpass.getpass(prompt='Enter Password > ')
    return email_user.strip(), pwd.strip()


def login_to_mail_server():
    print(f'DEBUG:: Enter login to mail server')


def get_email_registrations():
    print('DEBUG:: getting emails')


def create_csv():
    print("create csv")
