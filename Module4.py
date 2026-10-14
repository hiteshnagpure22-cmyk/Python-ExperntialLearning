# Module 4: Integrated Menu-Driven System
import sys
import subprocess
import os

from Module1 import add_contact
from Module2 import view_contacts, search_contact
from Module3 import update_contact, delete_contact

def show_project_banner():
    print("=" * 55)
    print("        CONTACT MANAGEMENT SYSTEM")
    print("=" * 55)

def launch_web_server():
    print("\nStarting Web Application on http://127.0.0.1:5000 ...")
    app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")
    try:
        subprocess.run([sys.executable, app_path])
    except KeyboardInterrupt:
        print("\nWeb server stopped.")
    except Exception as e:
        print(f"Error launching web server: {e}")

def main():
    show_project_banner()
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Launch Web Interface (Browser)")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

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
            launch_web_server()
        elif choice == "7":
            print("\nThank you for using Contact Management System!")
            break
        else:
            print("\n[!] Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()