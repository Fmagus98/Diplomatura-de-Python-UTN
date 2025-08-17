from peewee import SqliteDatabase, Model, CharField, AutoField
from model.user import User 

# Conexión a la base de datos
db = SqliteDatabase("users.db")

# Definimos el modelo ORM
class UserModel(Model):
    id = AutoField()
    name = CharField()
    dni = CharField()
    email = CharField()
    phone = CharField()
    photo = CharField(null=True)

    class Meta:
        database = db
        table_name = "users"

db.connect()
db.create_tables([UserModel])


class UserStorage:
    def __init__(self):
        pass  

    def create_user(self, name, dni, email, phone, photo=None):
        user_model = UserModel.create(
            name=name,
            dni=dni,
            email=email,
            phone=phone,
            photo=photo
        )
        return User(
            user_model.id,
            user_model.name,
            user_model.dni,
            user_model.email,
            user_model.phone,
            user_model.photo
        )

    def get_all_users(self):
        return [
            User(u.id, u.name, u.dni, u.email, u.phone, u.photo)
            for u in UserModel.select()
        ]

    def get_user_by_id(self, user_id):
        try:
            u = UserModel.get(UserModel.id == user_id)
            return User(u.id, u.name, u.dni, u.email, u.phone, u.photo)
        except UserModel.DoesNotExist:
            return None

    def update_user(self, user_id, name, dni, email, phone, photo=None):
        query = UserModel.update(
            name=name,
            dni=dni,
            email=email,
            phone=phone,
            photo=photo
        ).where(UserModel.id == user_id)
        query.execute()
        return self.get_user_by_id(user_id)

    def delete_user(self, user_id):
        deleted = UserModel.delete().where(UserModel.id == user_id).execute()
        return deleted > 0
