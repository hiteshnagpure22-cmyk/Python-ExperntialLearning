# MODULE 3
# Update and Delete Contacts

FILE_NAME = "contacts.txt"


def update_contact():
    print("\n========== UPDATE CONTACT ==========")

    search = input("Enter Name or Mobile Number of contact to update: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        found = False

        for i in range(len(contacts)):
            data = contacts[i].strip().split("|")

            if len(data) == 5:

                name = data[0].lower()
                mobile = data[1]

                if search == name or search == mobile:

                    print("\nContact Found!")
                    print("Enter new details:")

                    new_name = input("Enter Name: ")
                    new_mobile = input("Enter Mobile Number: ")
                    new_email = input("Enter Email: ")
                    new_address = input("Enter Address: ")
                    new_organization = input("Enter Organization: ")

                    updated_contact = (
                        new_name + "|" +
                        new_mobile + "|" +
                        new_email + "|" +
                        new_address + "|" +
                        new_organization + "\n"
                    )

                    contacts[i] = updated_contact

                    found = True
                    break

        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(contacts)

            print("\nContact updated successfully!")

        else:
            print("\nContact not found.")

    except FileNotFoundError:
        print("No contacts found.")


def delete_contact():
    print("\n========== DELETE CONTACT ==========")

    search = input("Enter Name or Mobile Number of contact to delete: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        new_contacts = []
        found = False

        for contact in contacts:
            data = contact.strip().split("|")

            if len(data) == 5:

                name = data[0].lower()
                mobile = data[1]

                if search == name or search == mobile:
                    found = True
                else:
                    new_contacts.append(contact)

        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(new_contacts)

            print("\nContact deleted successfully!")

        else:
            print("\nContact not found.")

    except FileNotFoundError:
        print("No contacts found.")
