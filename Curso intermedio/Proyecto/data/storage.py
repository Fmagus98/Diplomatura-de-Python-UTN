from model.user import User

class UserStorage:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def create_user(self, name, email):
        user = User(self.next_id, name, email)
        self.users[self.next_id] = user
        self.next_id += 1
        return user

    def get_all_users(self):
        return list(self.users.values())

    def update_user(self, user_id, name, email):
        if user_id in self.users:
            self.users[user_id].name = name
            self.users[user_id].email = email
            return True
        return False

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
