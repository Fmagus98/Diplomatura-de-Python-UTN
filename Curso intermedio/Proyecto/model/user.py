class User:
    def __init__(self, user_id: int, name: str, dni: int, email: str, phone: int, photo: str = None):
        self.id = user_id
        self.name = name
        self.dni = dni
        self.email = email
        self.phone = phone
        self.photo = photo

    def to_dict(self):
        return {"id": self.id, "name": self.name, self.dni:"dni", "email": self.email, "phone":self.phone, "photo": self.photo}
