from database import (
    create_tables,
    add_donor,
    add_recipient,
    get_donors_by_blood_group,
    get_all_donors,
    get_all_recipients,
    update_donor_availability
)

from donor import Donor
from recipient import Recipient


def register_donor():
    print("\n--- Register Donor ---")

    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        blood_group = input("Enter blood group: ")
        phone = input("Enter phone number: ")
        city = input("Enter city: ")

        donor = Donor(
            name, age, gender,
            blood_group, phone, city
        )

        valid, message = donor.validate()

        if valid:
            add_donor(donor)
            print("\nDonor registered successfully!")
        else:
            print("\nError:", message)

    except ValueError:
        print("\nPlease enter a valid age.")


def register_recipient():
    print("\n--- Register Recipient ---")

    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        blood_group = input("Enter blood group: ")
        phone = input("Enter phone number: ")
        city = input("Enter city: ")

        recipient = Recipient(
            name, age,
            blood_group, phone, city
        )

        valid, message = recipient.validate()

        if valid:
            add_recipient(recipient)
            print("\nRecipient registered successfully!")
        else:
            print("\nError:", message)

    except ValueError:
        print("\nPlease enter a valid age.")


def search_donors():
    print("\n--- Search Available Donors ---")

    blood_group = input(
        "Enter required blood group: "
    ).upper()

    if blood_group not in Donor.blood_groups():
        print("\nInvalid blood group.")
        return

    donors = get_donors_by_blood_group(blood_group)

    if len(donors) == 0:
        print("\nNo available donors found.")
        return

    print("\nAvailable Donors:")

    for donor in donors:
        print("-----------------------------")
        print("Donor ID:", donor[0])
        print("Name:", donor[1])
        print("Age:", donor[2])
        print("Gender:", donor[3])
        print("Blood Group:", donor[4])
        print("Phone:", donor[5])
        print("City:", donor[6])


def show_all_donors():
    print("\n--- All Registered Donors ---")

    donors = get_all_donors()

    if len(donors) == 0:
        print("No donors registered yet.")
        return

    for donor in donors:
        print("\n-----------------------------")
        print("Donor ID:", donor[0])
        print("Name:", donor[1])
        print("Age:", donor[2])
        print("Gender:", donor[3])
        print("Blood Group:", donor[4])
        print("Phone:", donor[5])
        print("City:", donor[6])

        if donor[7] == 1:
            print("Availability: Available")
        else:
            print("Availability: Unavailable")

    print("\nTotal Donors:", len(donors))


def show_all_recipients():
    print("\n--- All Registered Recipients ---")

    recipients = get_all_recipients()

    if len(recipients) == 0:
        print("No recipients registered yet.")
        return

    for recipient in recipients:
        print("\n-----------------------------")
        print("Recipient ID:", recipient[0])
        print("Name:", recipient[1])
        print("Age:", recipient[2])
        print("Blood Group:", recipient[3])
        print("Phone:", recipient[4])
        print("City:", recipient[5])

    print("\nTotal Recipients:", len(recipients))


def change_donor_status():
    print("\n--- Update Donor Availability ---")

    try:
        donor_id = int(input("Enter donor ID: "))
        status = input(
            "Available? (yes/no): "
        ).lower()

        if status == "yes":
            update_donor_availability(donor_id, 1)
            print("\nDonor marked as available.")

        elif status == "no":
            update_donor_availability(donor_id, 0)
            print("\nDonor marked as unavailable.")

        else:
            print("\nPlease enter yes or no.")

    except ValueError:
        print("\nPlease enter a valid donor ID.")


def menu():
    create_tables()

    while True:
        print("\n==============================")
        print("     BLOOD DONATION SYSTEM")
        print("==============================")
        print("1. Register Donor")
        print("2. Register Recipient")
        print("3. Search Available Donors")
        print("4. Show All Donors")
        print("5. Show All Recipients")
        print("6. Update Donor Availability")
        print("7. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_donor()

        elif choice == "2":
            register_recipient()

        elif choice == "3":
            search_donors()

        elif choice == "4":
            show_all_donors()

        elif choice == "5":
            show_all_recipients()

        elif choice == "6":
            change_donor_status()

        elif choice == "7":
            print("\nThank you for using")
            print("Blood Donation System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    menu()