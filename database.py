import sqlite3

DATABASE = "blood_bank.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors (
            donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            blood_group TEXT NOT NULL,
            phone TEXT NOT NULL,
            city TEXT NOT NULL,
            available INTEGER DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipients (
            recipient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            blood_group TEXT NOT NULL,
            phone TEXT NOT NULL,
            city TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_donor(donor):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO donors
        (name, age, gender, blood_group, phone, city, available)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        donor.name,
        donor.age,
        donor.gender,
        donor.blood_group,
        donor.phone,
        donor.city,
        donor.available
    ))

    conn.commit()
    conn.close()


def add_recipient(recipient):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO recipients
        (name, age, blood_group, phone, city)
        VALUES (?, ?, ?, ?, ?)
    """, (
        recipient.name,
        recipient.age,
        recipient.blood_group,
        recipient.phone,
        recipient.city
    ))

    conn.commit()
    conn.close()


def get_donors_by_blood_group(blood_group):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM donors
        WHERE blood_group = ? AND available = 1
    """, (blood_group.upper(),))

    donors = cursor.fetchall()
    conn.close()

    return donors


def get_all_donors():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()

    conn.close()
    return donors


def get_all_recipients():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipients")
    recipients = cursor.fetchall()

    conn.close()
    return recipients


def update_donor_availability(donor_id, status):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE donors
        SET available = ?
        WHERE donor_id = ?
    """, (status, donor_id))

    conn.commit()
    conn.close()