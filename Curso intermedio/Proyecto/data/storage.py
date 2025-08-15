from model.user import User

class UserStorage:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def create_user(self, name, email, photo=None):
        user = User(self.next_id, name, email, photo)
        self.users[self.next_id] = user
        self.next_id += 1
        return user

    def get_all_users(self):
        return list(self.users.values())

    def update_user(self, user_id, name, email, photo=None):
        for user in self.users:
            if user.id == user_id:
                user.name = name
                user.email = email
                if photo is not None:
                    user.photo = photo
                return user
        return None

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
