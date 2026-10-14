# Module 2: View Saved Contacts and Search by Details
# Author: Hitesh Nagpure (USN: CD25085, CSE-DS, S.B. Jain Institute)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "contacts.txt")

def get_all_contacts():
    """
    Reads all contacts from contacts.txt and returns a list of dicts.
    Each item includes index/id, name, mobile, email, address, and organization.
    """
    contacts_list = []
    if not os.path.exists(FILE_NAME):
        return contacts_list

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            data = line.split("|")
            if len(data) >= 5:
                contacts_list.append({
                    "id": idx,
                    "name": data[0].strip(),
                    "mobile": data[1].strip(),
                    "email": data[2].strip(),
                    "address": data[3].strip(),
                    "organization": data[4].strip()
                })
    except Exception as e:
        print(f"Error reading contacts: {e}")

    return contacts_list

def search_contacts_data(query):
    """
    Searches contacts by Name or Mobile Number (case-insensitive).
    Also supports partial matches and email/organization.
    """
    query = (query or "").strip().lower()
    if not query:
        return get_all_contacts()

    all_contacts = get_all_contacts()
    results = []

    for contact in all_contacts:
        name = contact["name"].lower()
        mobile = contact["mobile"].lower()
        email = contact["email"].lower()
        org = contact["organization"].lower()

        if query in name or query in mobile or query in email or query in org:
            results.append(contact)

    return results

def view_contacts():
    """CLI interface to view all saved contacts."""
    print("\n========== ALL CONTACTS (MODULE 2) ==========")
    contacts = get_all_contacts()

    if not contacts:
        print("No contacts available.")
        return

    for count, contact in enumerate(contacts, start=1):
        print(f"\n--- Contact {count} ---")
        print("Name          :", contact["name"])
        print("Mobile Number :", contact["mobile"])
        print("Email         :", contact["email"])
        print("Address       :", contact["address"])
        print("Organization  :", contact["organization"])

    print(f"\nTotal Contacts: {len(contacts)}")

def search_contact():
    """CLI interface to search contacts."""
    print("\n========== SEARCH CONTACT (MODULE 2) ==========")
    search = input("Enter Name or Mobile Number: ")

    results = search_contacts_data(search)

    if not results:
        print("\nContact not found.")
        return

    print(f"\nFound {len(results)} matching contact(s):")
    for count, contact in enumerate(results, start=1):
        print(f"\n[Result {count}]")
        print("Name          :", contact["name"])
        print("Mobile Number :", contact["mobile"])
        print("Email         :", contact["email"])
        print("Address       :", contact["address"])
        print("Organization  :", contact["organization"])

if __name__ == "__main__":
    view_contacts()
    search_contact()