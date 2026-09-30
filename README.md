# MODULE 1
# Add and Store Contacts

FILE_NAME = "contacts.txt"


def add_contact():
    print("\n========== ADD CONTACT ==========")

    name = input("Enter Name: ")
    mobile = input("Enter Mobile Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    organization = input("Enter Organization: ")

    contact = name + "|" + mobile + "|" + email + "|" + address + "|" + organization

    with open(FILE_NAME, "a") as file:
        file.write(contact + "\n")

    print("\nContact added successfully!")
