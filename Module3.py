# Module 3: Update or Delete Stored Contacts
# Author: Hitesh Nagpure (USN: CD25085, CSE-DS, S.B. Jain Institute)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "contacts.txt")

def update_contact_by_index(target_index, new_name, new_mobile, new_email, new_address, new_organization):
    """Updates a contact at a specific line index in contacts.txt."""
    if not os.path.exists(FILE_NAME):
        return False, "File not found."

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        valid_entries = []
        for idx, line in enumerate(lines):
            line_str = line.strip()
            if line_str and len(line_str.split("|")) >= 5:
                valid_entries.append((idx, line))

        if target_index < 0 or target_index >= len(valid_entries):
            return False, "Contact not found."

        actual_file_line = valid_entries[target_index][0]

        safe_name = new_name.strip().replace('|', '/')
        safe_mobile = new_mobile.strip().replace('|', '/')
        safe_email = new_email.strip().replace('|', '/')
        safe_address = new_address.strip().replace('|', '/')
        safe_org = new_organization.strip().replace('|', '/')

        lines[actual_file_line] = f"{safe_name}|{safe_mobile}|{safe_email}|{safe_address}|{safe_org}\n"

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.writelines(lines)

        return True, "Contact updated successfully!"
    except Exception as e:
        return False, f"Failed to update contact: {str(e)}"

def delete_contact_by_index(target_index):
    """Deletes a contact at a specific line index in contacts.txt."""
    if not os.path.exists(FILE_NAME):
        return False, "File not found."

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        valid_entries = []
        for idx, line in enumerate(lines):
            line_str = line.strip()
            if line_str and len(line_str.split("|")) >= 5:
                valid_entries.append((idx, line))

        if target_index < 0 or target_index >= len(valid_entries):
            return False, "Contact not found."

        actual_file_line = valid_entries[target_index][0]
        del lines[actual_file_line]

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.writelines(lines)

        return True, "Contact deleted successfully!"
    except Exception as e:
        return False, f"Failed to delete contact: {str(e)}"

def update_contact():
    """CLI interface to update contact."""
    print("\n========== UPDATE CONTACT (MODULE 3) ==========")
    search = input("Enter Name or Mobile Number of contact to update: ").strip().lower()

    if not os.path.exists(FILE_NAME):
        print("No contacts file found.")
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            contacts = file.readlines()

        found = False
        for i in range(len(contacts)):
            data = contacts[i].strip().split("|")
            if len(data) >= 5:
                name = data[0].strip().lower()
                mobile = data[1].strip()

                if search == name or search == mobile:
                    print("\nContact Found!")
                    print(f"Current Name: {data[0]}")
                    print(f"Current Mobile: {data[1]}")
                    print(f"Current Email: {data[2]}")
                    print(f"Current Address: {data[3]}")
                    print(f"Current Organization: {data[4]}")

                    print("\nEnter new details (or leave blank to keep unchanged):")
                    new_name = input("Enter Name: ").strip() or data[0]
                    new_mobile = input("Enter Mobile Number: ").strip() or data[1]
                    new_email = input("Enter Email: ").strip() or data[2]
                    new_address = input("Enter Address: ").strip() or data[3]
                    new_organization = input("Enter Organization: ").strip() or data[4]

                    updated_contact = (
                        f"{new_name.replace('|', '/')}|"
                        f"{new_mobile.replace('|', '/')}|"
                        f"{new_email.replace('|', '/')}|"
                        f"{new_address.replace('|', '/')}|"
                        f"{new_organization.replace('|', '/')}\n"
                    )

                    contacts[i] = updated_contact
                    found = True
                    break

        if found:
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                file.writelines(contacts)
            print("\nContact updated successfully!")
        else:
            print("\nContact not found.")

    except Exception as e:
        print(f"Error: {e}")

def delete_contact():
    """CLI interface to delete contact."""
    print("\n========== DELETE CONTACT (MODULE 3) ==========")
    search = input("Enter Name or Mobile Number of contact to delete: ").strip().lower()

    if not os.path.exists(FILE_NAME):
        print("No contacts file found.")
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            contacts = file.readlines()

        new_contacts = []
        found = False

        for contact in contacts:
            data = contact.strip().split("|")
            if len(data) >= 5:
                name = data[0].strip().lower()
                mobile = data[1].strip()

                if (search == name or search == mobile) and not found:
                    found = True
                    print(f"Deleting contact: {data[0]} ({data[1]})")
                else:
                    new_contacts.append(contact)
            else:
                new_contacts.append(contact)

        if found:
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                file.writelines(new_contacts)
            print("\nContact deleted successfully!")
        else:
            print("\nContact not found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_contact()