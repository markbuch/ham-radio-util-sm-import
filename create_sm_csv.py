# imports
import funcs
import datetime as dt
import logging
#  main entry point


def main():
    current_choice = None

    # Define main menu options.  "0" will be used for exit.
    available_choices = {
        "1": "Add Signing VEs",
        "2": "Enter Mail Server",
        "3": "Enter Login Credentials",
        "4": "Get Registered users and Create CSV",
    }
    # certifying_ves = None
    while current_choice != "0":

        if current_choice in available_choices:
            print(f"DEBUG:: Current Choice: {current_choice}")
            if current_choice == "1":
                certifying_ves = funcs.get_certifying_ves()
                if len(certifying_ves) != 3:
                    print(f"A total of 3 VEs are required.  Exiting program, please try again.")
                    break
                print(f"You entered the following VEs: {certifying_ves}")
                print()
                current_choice = None
                continue
            elif current_choice == "2":
                funcs.get_mail_server()
                print()
                current_choice = None
                continue
            elif current_choice == "3":
                funcs.get_login_creds()
                print()
                current_choice = None
                continue
            elif current_choice == "4":
                # Login
                # Retrieved registered applicants
                # Process downloads
                # create csv
                funcs.create_csv()
                print()
                current_choice = None
                continue

            else:
                print("DEBUG:: Reprint Menu.")

        else:
            # Display the menu
            funcs.print_menu(available_choices)
        current_choice = input("> ")


if __name__ == "__main__":
    main()
