# MODULE 4
# Complete Menu-Driven Contact Management System

from module1_add import add_contact
from module2_view_search import view_contacts, search_contact
from module3_update_delete import update_contact, delete_contact


def main():

    while True:

        print("\n")
        print("======================================")
        print("     CONTACTS LIST MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("\nThank you for using Contact Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()
