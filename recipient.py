class Recipient:
    VALID_BLOOD_GROUPS = [
        "A+", "A-", "B+", "B-",
        "AB+", "AB-", "O+", "O-"
    ]

    def __init__(self, name, age, blood_group, phone, city):
        self.name = name
        self.age = age
        self.blood_group = blood_group.upper()
        self.phone = phone
        self.city = city

    def validate(self):
        if not self.name.strip():
            return False, "Name cannot be empty."

        if self.age <= 0:
            return False, "Age must be valid."

        if self.blood_group not in self.VALID_BLOOD_GROUPS:
            return False, "Invalid blood group."

        if not self.phone.isdigit() or len(self.phone) != 10:
            return False, "Phone number must contain 10 digits."

        if not self.city.strip():
            return False, "City cannot be empty."

        return True, "Valid recipient."

    def display(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Blood Group: {self.blood_group}\n"
            f"Phone: {self.phone}\n"
            f"City: {self.city}"
        )