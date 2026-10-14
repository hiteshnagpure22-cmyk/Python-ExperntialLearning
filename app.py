# Contacts Management System - Web Application
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
import sys

# Ensure local directory is in path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from Module1 import save_contact_record, FILE_NAME
from Module2 import get_all_contacts, search_contacts_data
from Module3 import update_contact_by_index, delete_contact_by_index

app = Flask(__name__)
app.secret_key = "contact-management-secret-key"

@app.context_processor
def inject_global_data():
    """Provides application-wide properties."""
    return {
        "app_title": "Contact Management System",
        "storage_file": "contacts.txt"
    }

# ----------------- DASHBOARD -----------------
@app.route("/")
def index():
    contacts = get_all_contacts()
    total_count = len(contacts)
    personal_count = sum(1 for c in contacts if c["organization"].lower() in ["personal", "self", "none", "family", "friend"])
    professional_count = total_count - personal_count
    
    return render_template(
        "index.html",
        contacts=contacts[:6], # preview latest 6
        total_count=total_count,
        personal_count=personal_count,
        professional_count=professional_count
    )

# ----------------- ADD CONTACT -----------------
@app.route("/add", methods=["GET", "POST"])
@app.route("/module1", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        mobile = request.form.get("mobile", "").strip()
        email = request.form.get("email", "").strip()
        address = request.form.get("address", "").strip()
        organization = request.form.get("organization", "").strip() or "Personal"

        if not name or not mobile:
            flash("Name and Mobile Number are required fields.", "danger")
            return render_template("add_contact.html", form_data=request.form)

        # Check for duplicate mobile
        all_contacts = get_all_contacts()
        for c in all_contacts:
            if c["mobile"] == mobile:
                flash(f"A contact with mobile number {mobile} already exists ({c['name']})!", "warning")
                return render_template("add_contact.html", form_data=request.form)

        success, message = save_contact_record(name, mobile, email, address, organization)
        if success:
            flash(f"Contact '{name}' added successfully!", "success")
            return redirect(url_for("view_contacts"))
        else:
            flash(message, "danger")
            return render_template("add_contact.html", form_data=request.form)

    return render_template("add_contact.html", form_data={})

# ----------------- SEARCH & VIEW CONTACTS -----------------
@app.route("/search")
@app.route("/contacts")
@app.route("/module2")
def view_contacts():
    query = request.args.get("q", "").strip()
    if query:
        contacts = search_contacts_data(query)
    else:
        contacts = get_all_contacts()

    return render_template("view_contacts.html", contacts=contacts, search_query=query)

# ----------------- MANAGE (UPDATE & DELETE) -----------------
@app.route("/manage")
@app.route("/module3")
def manage_contacts():
    contacts = get_all_contacts()
    return render_template("manage_contacts.html", contacts=contacts)

# ----------------- UPDATE CONTACT -----------------
@app.route("/edit/<int:contact_id>", methods=["GET", "POST"])
@app.route("/module3/edit/<int:contact_id>", methods=["GET", "POST"])
def edit_contact(contact_id):
    contacts = get_all_contacts()
    target_contact = None
    for c in contacts:
        if c["id"] == contact_id:
            target_contact = c
            break

    if not target_contact:
        flash("Contact not found.", "danger")
        return redirect(url_for("manage_contacts"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        mobile = request.form.get("mobile", "").strip()
        email = request.form.get("email", "").strip()
        address = request.form.get("address", "").strip()
        organization = request.form.get("organization", "").strip() or "Personal"

        if not name or not mobile:
            flash("Name and Mobile Number cannot be blank.", "danger")
            return render_template("edit_contact.html", contact=target_contact)

        success, msg = update_contact_by_index(contact_id, name, mobile, email, address, organization)
        if success:
            flash(f"Contact '{name}' updated successfully!", "success")
            return redirect(url_for("manage_contacts"))
        else:
            flash(msg, "danger")
            return render_template("edit_contact.html", contact=target_contact)

    return render_template("edit_contact.html", contact=target_contact)

# ----------------- DELETE CONTACT -----------------
@app.route("/delete/<int:contact_id>", methods=["POST"])
@app.route("/module3/delete/<int:contact_id>", methods=["POST"])
def delete_contact(contact_id):
    contacts = get_all_contacts()
    contact_name = "Contact"
    for c in contacts:
        if c["id"] == contact_id:
            contact_name = c["name"]
            break

    success, msg = delete_contact_by_index(contact_id)
    if success:
        flash(f"Contact '{contact_name}' deleted successfully!", "success")
    else:
        flash(msg, "danger")
    return redirect(url_for("manage_contacts"))

# ----------------- REST API ENDPOINTS -----------------
@app.route("/api/contacts", methods=["GET"])
def api_get_contacts():
    contacts = get_all_contacts()
    return jsonify({"success": True, "count": len(contacts), "data": contacts})

@app.route("/api/contacts/search", methods=["GET"])
def api_search_contacts():
    q = request.args.get("q", "")
    results = search_contacts_data(q)
    return jsonify({"success": True, "query": q, "count": len(results), "data": results})

@app.route("/api/contacts", methods=["POST"])
def api_add_contact():
    data = request.get_json() or {}
    name = data.get("name", "").strip()
    mobile = data.get("mobile", "").strip()
    email = data.get("email", "").strip()
    address = data.get("address", "").strip()
    organization = data.get("organization", "Personal").strip()

    if not name or not mobile:
        return jsonify({"success": False, "message": "Name and Mobile are required"}), 400

    success, msg = save_contact_record(name, mobile, email, address, organization)
    return jsonify({"success": success, "message": msg}), (201 if success else 400)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("=" * 60)
    print(f" Contact Management System - Running on port {port}")
    print("=" * 60)
    app.run(debug=False, host="0.0.0.0", port=port)
