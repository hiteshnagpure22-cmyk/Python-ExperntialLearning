# Module 1: Add and Store Contact Details
# Author: Hitesh Nagpure (USN: CD25085, CSE-DS, S.B. Jain Institute)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "contacts.txt")

def save_contact_record(name, mobile, email, address, organization):
    """
    Saves a contact record to the contacts.txt file in pipe-delimited format.
    Returns (True, message) on success or (False, error) on failure.
    """
    name = name.strip()
    mobile = mobile.strip()
    email = email.strip()
    address = address.strip()
    organization = organization.strip()

    if not name or not mobile:
        return False, "Name and Mobile number are required fields."

    # Avoid delimiter conflict by replacing any accidental pipes
    record = f"{name.replace('|', '/')}|{mobile.replace('|', '/')}|{email.replace('|', '/')}|{address.replace('|', '/')}|{organization.replace('|', '/')}\n"

    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(record)
        return True, "Contact added successfully!"
    except Exception as e:
        return False, f"Failed to save contact: {str(e)}"

def add_contact():
    """CLI interface to add a contact."""
    print("\n========== ADD CONTACT (MODULE 1) ==========")
    name = input("Enter Name: ")
    mobile = input("Enter Mobile Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    organization = input("Enter Organization: ")

    success, msg = save_contact_record(name, mobile, email, address, organization)
    if success:
        print(f"\n[SUCCESS] {msg}")
    else:
        print(f"\n[ERROR] {msg}")

if __name__ == "__main__":
    add_contact()