import flet as ft
from controller.user_controller import UserController
from utils.opencv_photo import capture_face_photo  # Ajusta la ruta si es necesario

class FletView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.controller = UserController()

        # Campos de entrada
        self.name_field = ft.TextField(label="Nombre")
        self.dni_field = ft.TextField(label="DNI", keyboard_type="number")
        self.email_field = ft.TextField(label="Email")
        self.phone_field = ft.TextField(label="Teléfono", hint_text="Ingresa tu teléfono", keyboard_type="phone")

        # Buscador
        self.search_field = ft.TextField(
            label="Buscar usuario",
            hint_text="Buscar por nombre, DNI, email o teléfono",
            on_change=self.search_users
        )

        # Selección de imagen
        self.file_picker = ft.FilePicker(on_result=self.file_picker_result)
        self.page.overlay.append(self.file_picker)

        self.photo_path = None

        self.photo_button = ft.ElevatedButton("Seleccionar Foto", on_click=self.open_file_picker)
        self.photo_button_web = ft.ElevatedButton("Tomar foto con webcam", on_click=self.capture_photo_from_webcam)
        self.photo_preview = ft.Image(width=100, height=100)

        self.user_list = ft.Column()
        self.selected_user_id = None

        self.page.title = "CRUD Flet MVC"
        self.page.scroll = "auto"

        # Construcción UI
        self.refresh_user_list()
        self.page.add(
            self.name_field,
            self.dni_field,
            self.email_field,
            self.phone_field,
            ft.Row([self.photo_button, self.photo_preview, self.photo_button_web]),
            ft.Row([
                ft.ElevatedButton("Crear", on_click=self.create_user),
                ft.ElevatedButton("Actualizar", on_click=self.update_user),
            ]),
            self.search_field,  # Buscador aquí
            ft.Text("Usuarios:"),
            self.user_list
        )

    def open_file_picker(self, e):
        self.file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "jpg", "jpeg"])

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]
            self.photo_path = file.path
            self.photo_preview.src = self.photo_path
            self.page.update()

    def create_user(self, e):
        name = self.name_field.value
        dni = self.dni_field.value
        phone = self.phone_field.value
        email = self.email_field.value
        photo = self.photo_path
        if name and email:
            self.controller.create_user(name, dni, email, phone, photo)
            self.clear_fields()
            self.refresh_user_list()

    def update_user(self, e):
        if self.selected_user_id:
            name = self.name_field.value
            dni = self.dni_field.value
            email = self.email_field.value
            phone = self.phone_field.value
            photo = self.photo_path
            self.controller.update_user(self.selected_user_id, name, dni, email, phone, photo)
            self.selected_user_id = None
            self.clear_fields()
            self.refresh_user_list()

    def delete_user(self, e, user_id):
        self.controller.delete_user(user_id)
        self.refresh_user_list()

    def select_user(self, e, user):
        self.selected_user_id = user.id
        self.name_field.value = user.name
        self.dni_field.value = user.dni
        self.email_field.value = user.email
        self.phone_field.value = user.phone
        self.photo_path = user.photo
        self.photo_preview.src = self.photo_path
        self.page.update()

    def refresh_user_list(self):
        users = self.controller.get_users()
        self.display_user_list(users)

    def display_user_list(self, users):
        self.user_list.controls.clear()
        for user in users:
            row = ft.Row([
                ft.Image(src=user.photo or "", width=50, height=50),
                ft.Text(f"{user.id}. {user.name} - {user.dni} - {user.email} - {user.phone}"),
                ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, u=user: self.select_user(e, u)),
                ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, uid=user.id: self.delete_user(e, uid))
            ])
            self.user_list.controls.append(row)
        self.page.update()

    def search_users(self, e):
        query = self.search_field.value.lower()
        filtered_users = []

        for user in self.controller.get_users():
            if (
                query in user.name.lower()
                or query in str(user.dni).lower()
                or query in user.email.lower()
                or query in str(user.phone).lower()
            ):
                filtered_users.append(user)

        self.display_user_list(filtered_users)

    def clear_fields(self):
        self.name_field.value = ""
        self.dni_field.value = None
        self.email_field.value = ""
        self.phone_field.value = None
        self.photo_path = None
        self.photo_preview.src = None
        self.page.update()

    def capture_photo_from_webcam(self, e):
        photo_path = capture_face_photo()
        if photo_path:
            self.photo_path = photo_path
            self.photo_preview.src = photo_path
            self.page.update()
        else:
            print("No se capturó una imagen válida desde la webcam.")
