# MODULE 2
# View and Search Contacts

FILE_NAME = "contacts.txt"


def view_contacts():
    print("\n========== ALL CONTACTS ==========")

    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        if len(contacts) == 0:
            print("No contacts available.")
            return

        count = 1

        for contact in contacts:
            data = contact.strip().split("|")

            if len(data) == 5:
                print("\nContact", count)
                print("Name          :", data[0])
                print("Mobile Number :", data[1])
                print("Email         :", data[2])
                print("Address       :", data[3])
                print("Organization  :", data[4])

                count += 1

    except FileNotFoundError:
        print("No contacts found.")


def search_contact():
    print("\n========== SEARCH CONTACT ==========")

    search = input("Enter Name or Mobile Number: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        found = False

        for contact in contacts:
            data = contact.strip().split("|")

            if len(data) == 5:

                name = data[0].lower()
                mobile = data[1]

                if search == name or search == mobile:
                    print("\nContact Found!")
                    print("Name          :", data[0])
                    print("Mobile Number :", data[1])
                    print("Email         :", data[2])
                    print("Address       :", data[3])
                    print("Organization  :", data[4])

                    found = True

        if not found:
            print("\nContact not found.")

    except FileNotFoundError:
        print("No contacts found.")
