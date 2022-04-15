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
        print(f"Len() of ve: {len(ve)}")
        if len(ve) <= 3 or len(ve) > 6:
            print("An INVALID call sign was entered.")
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
        if ve == "cancel":
            return "NONE"

        ve_list.append(ve)
        print(f"ve_list: {ve_list}")
    #  return list of VEs as a Tuple, since list of VEs need to maintain order.
    return tuple(ve_list)

    # Get VE #1
    # print("Getting VE 1")
    # ve = get_ve(1)
    # if ve == "cancel":
    #     return "cancel"
    #
    # ve_list.append(ve)
    # print(f"ve_list: {ve_list}")
    #
    # # Get Ve #2
    # print("Getting VE 2")
    # ve = get_ve(1)
    # if ve == "cancel":
    #     return "cancel"
    #
    # ve_list.append(ve)
    # print(f"ve_list: {ve_list}")
    #
    # # Get VE #3
    # print("Getting VE 3")
    # ve = get_ve(1)
    # if ve == "cancel":
    #     return "cancel"
    #
    # ve_list.append(ve)
    # print(f"ve_list: {ve_list}")
    #
    # #  return list of VEs as a Tuple, since list of VEs need to maintain order.
    # return tuple(ve_list)


def get_mail_server():
    print("DEBUG:: Get Mail Server address")
    mail_server = input("Enter the mail server URL > ")
    choice = input(f"You entered {mail_server}. Is that correct? Y/N, Press C to Cancel.")
    if choice.upper() == "C":
        print("Exiting to Main Menu.  Press ENTER to continue.")
        return

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
