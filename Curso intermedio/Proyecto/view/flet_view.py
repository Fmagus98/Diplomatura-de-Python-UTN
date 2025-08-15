import flet as ft
from controller.user_controller import UserController


class FletView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.controller = UserController()

        self.name_field = ft.TextField(label="Nombre")
        self.email_field = ft.TextField(label="Email")
        self.user_list = ft.Column()
        self.selected_user_id = None

        self.page.title = "CRUD Flet MVC"
        self.page.scroll = "auto"

        self.refresh_user_list()
        self.page.add(
            self.name_field,
            self.email_field,
            ft.Row([
                ft.ElevatedButton("Crear", on_click=self.create_user),
                ft.ElevatedButton("Actualizar", on_click=self.update_user),
            ]),
            ft.Text("Usuarios:"),
            self.user_list
        )

    def create_user(self, e):
        name = self.name_field.value
        email = self.email_field.value
        if name and email:
            self.controller.create_user(name, email)
            self.name_field.value = ""
            self.email_field.value = ""
            self.refresh_user_list()
            self.page.update()

    def update_user(self, e):
        if self.selected_user_id:
            name = self.name_field.value
            email = self.email_field.value
            self.controller.update_user(self.selected_user_id, name, email)
            self.selected_user_id = None
            self.name_field.value = ""
            self.email_field.value = ""
            self.refresh_user_list()
            self.page.update()

    def delete_user(self, e, user_id):
        self.controller.delete_user(user_id)
        self.refresh_user_list()
        self.page.update()

    def select_user(self, e, user):
        self.selected_user_id = user.id
        self.name_field.value = user.name
        self.email_field.value = user.email
        self.page.update()

    def refresh_user_list(self):
        self.user_list.controls.clear()
        for user in self.controller.get_users():
            row = ft.Row([
                ft.Text(f"{user.id}. {user.name} - {user.email}"),
                ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, u=user: self.select_user(e, u)),
                ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, uid=user.id: self.delete_user(e, uid))
            ])
            self.user_list.controls.append(row)
