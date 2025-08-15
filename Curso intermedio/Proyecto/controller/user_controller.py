from data.storage import UserStorage

class UserController:
    def __init__(self):
        self.storage = UserStorage()

    def create_user(self, name, email, photo=None):
        return self.storage.create_user(name, email, photo)

    def get_users(self):
        return self.storage.get_all_users()

    def update_user(self, user_id, name, email, photo=None):
        return self.storage.update_user(user_id, name, email, photo)

    def delete_user(self, user_id):
        return self.storage.delete_user(user_id)
    
