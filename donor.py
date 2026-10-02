class Donor:
    VALID_BLOOD_GROUPS = [
        "A+", "A-", "B+", "B-",
        "AB+", "AB-", "O+", "O-"
    ]

    def __init__(self, name, age, gender, blood_group, phone, city):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_group = blood_group.upper()
        self.phone = phone
        self.city = city
        self.available = 1

    def validate(self):
        if not self.name.strip():
            return False, "Name cannot be empty."

        if self.age < 18 or self.age > 65:
            return False, "Donor age must be between 18 and 65."

        if self.blood_group not in self.VALID_BLOOD_GROUPS:
            return False, "Invalid blood group."

        if not self.phone.isdigit() or len(self.phone) != 10:
            return False, "Phone number must contain 10 digits."

        if not self.city.strip():
            return False, "City cannot be empty."

        return True, "Valid donor."

    def display(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Blood Group: {self.blood_group}\n"
            f"Phone: {self.phone}\n"
            f"City: {self.city}"
        )

    @staticmethod
    def blood_groups():
        return Donor.VALID_BLOOD_GROUPS