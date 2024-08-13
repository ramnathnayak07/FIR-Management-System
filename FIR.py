import getpass

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # Check if the username and password are correct
    if username == "admin" and password == "admin123":
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False

def add_record():
    fir_number = input("Enter FIR number: ")
    with open("criminal_records.txt", "r") as file:
        for line in file:
            record = line.strip().split("|")
            if record[0] == fir_number:
                print("Record with FIR number", fir_number, "already exists.")
                return
    name = input("Enter criminal's name: ")
    gender = input("Enter criminal's gender: ")
    age = input("Enter criminal's age: ")
    crime = input("Enter the crime committed: ")
    section = input("Enter the section of the crime: ")
    height = input("Enter criminal's height: ")
    weight = input("Enter criminal's weight: ")
    punishment = input("Enter the punishment: ")
    address = input("Enter criminal's address: ")
    contact = input("Enter criminal's contact: ")
    arrival_date = input("Enter arrival date: ")
    
    record = [fir_number, name, gender, age, crime, section, height, weight, punishment, address, contact, arrival_date]

    with open("criminal_records.txt", "a") as file:
        file.write("|".join(record) + "\n")
    print("Record added successfully.")

def delete_record():
    fir_number = input("Enter the FIR number of the record you want to delete: ")

    records = []
    found = False

    with open("criminal_records.txt", "r") as file:
        for line in file:
            record = line.strip().split("|")
            if record[0] == fir_number:
                found = True
                continue  # Skip the record to be deleted
            records.append(record)

    if found:
        with open("criminal_records.txt", "w") as file:
            for record in records:
                file.write("|".join(record) + "\n")
        print("Record deleted successfully.")
    else:
        print("Record with FIR number", fir_number, "does not exist.")

def search_record():
    fir_number = input("Enter the FIR number of the record you want to search: ")

    found = False
    with open("criminal_records.txt", "r") as file:
        for line in file:
            record = line.strip().split("|")
            if record[0] == fir_number:
                print("Record found:")
                print("FIR Number:", record[0])
                print("Name:", record[1])
                print("Gender:", record[2])
                print("Age:", record[3])
                print("Crime:", record[4])
                print("Section:", record[5])
                print("Height:", record[6])
                print("Weight:", record[7])
                print("Punishment:", record[8])
                print("Address:", record[9])
                print("Contact:", record[10])
                print("Arrival Date:", record[11])
                found = True
                break

    if not found:
        print("Record not found.")

def update_record():
    fir_number = input("Enter the FIR number of the record you want to update: ")

    records = []
    updated = False

    with open("criminal_records.txt", "r") as file:
        for line in file:
            record = line.strip().split("|")
            if record[0] == fir_number:
                print("Current record:")
                print("FIR Number:", record[0])
                print("Name:", record[1])
                print("Gender:", record[2])
                print("Age:", record[3])
                print("Crime:", record[4])
                print("Section:", record[5])
                print("Height:", record[6])
                print("Weight:", record[7])
                print("Punishment:", record[8])
                print("Address:", record[9])
                print("Contact:", record[10])
                print("Arrival Date:", record[11])

                name = input("Enter the updated name (press Enter to keep the current name): ")
                gender = input("Enter the updated gender (press Enter to keep the current gender): ")
                age = input("Enter the updated age (press Enter to keep the current age): ")
                crime = input("Enter the updated crime (press Enter to keep the current crime): ")
                section = input("Enter the updated section (press Enter to keep the current section): ")
                height = input("Enter the updated height (press Enter to keep the current height): ")
                weight = input("Enter the updated weight (press Enter to keep the current weight): ")
                punishment = input("Enter the updated punishment (press Enter to keep the current punishment): ")
                address = input("Enter the updated address (press Enter to keep the current address): ")
                contact = input("Enter the updated contact (press Enter to keep the current contact): ")
                arrival_date = input("Enter the updated arrival date (press Enter to keep the current arrival date): ")

                record[1] = name if name else record[1]
                record[2] = gender if gender else record[2]
                record[3] = age if age else record[3]
                record[4] = crime if crime else record[4]
                record[5] = section if section else record[5]
                record[6] = height if height else record[6]
                record[7] = weight if weight else record[7]
                record[8] = punishment if punishment else record[8]
                record[9] = address if address else record[9]
                record[10] = contact if contact else record[10]
                record[11] = arrival_date if arrival_date else record[11]

                updated = True

            records.append(record)

    if updated:
        with open("criminal_records.txt", "w") as file:
            for record in records:
                file.write("|".join(record) + "\n")
        print("Record updated successfully.")
    else:
        print("Record not found.")

def display_records():
    with open("criminal_records.txt", "r") as file:
        records = file.readlines()

    if not records:
        print("No records found.")
    else:
        print("Criminal records:")
        for record in records:
            record = record.strip().split("|")
            if len(record) >= 12:  # Ensure the record has all expected fields
                print("FIR Number:", record[0])
                print("Name:", record[1])
                print("Gender:", record[2])
                print("Age:", record[3])
                print("Crime:", record[4])
                print("Section:", record[5])
                print("Height:", record[6])
                print("Weight:", record[7])
                print("Punishment:", record[8])
                print("Address:", record[9])
                print("Contact:", record[10])
                print("Arrival Date:", record[11])
                print()

def main():
    logged_in = False

    while True:
        if not logged_in:
            print("Login required.")
            logged_in = login()
            if not logged_in:
                continue

        print("FIR Management System")
        print("---------------------")
        print("1. Add Record")
        print("2. Delete Record")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Display Records")
        print("6. Logout")
        choice = input("Enter your choice (1-6): ")
        print()

        if choice == '1':
            add_record()
        elif choice == '2':
            delete_record()
        elif choice == '3':
            search_record()
        elif choice == '4':
            update_record()
        elif choice == '5':
            display_records()
        elif choice == '6':
            logged_in = False
            print("Logged out successfully.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
