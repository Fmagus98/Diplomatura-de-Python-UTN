import flet as ft
from controller.user_controller import UserController
from utils.opencv_photo import capture_face_photo
from utils.regex import validate_name, validate_dni, validate_phone, validate_email
from utils.snackbar import show_snackbar

class FletView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.controller = UserController()

        self.page.title = "Gestión de Usuarios"
        self.page.scroll = "auto"
        self.page.padding = 20
        self.page.vertical_alignment = ft.MainAxisAlignment.START

        # === Campos de entrada ===
        self.name_field = ft.TextField(label="Nombre", expand=True)
        self.dni_field = ft.TextField(label="DNI", keyboard_type="number", expand=True)
        self.email_field = ft.TextField(label="Email", expand=True)
        self.phone_field = ft.TextField(label="Teléfono", keyboard_type="phone", expand=True)

        self.photo_path = "utils/img/captura_centrada.png"
        self.photo_preview = ft.Image(src="utils/img/captura_centrada.png", width=100, height=100, fit=ft.ImageFit.COVER)

        self.file_picker = ft.FilePicker(on_result=self.file_picker_result)
        self.page.overlay.append(self.file_picker)

        self.photo_button = ft.IconButton(icon=ft.icons.IMAGE, tooltip="Seleccionar Foto", on_click=self.open_file_picker)
        self.photo_button_web = ft.IconButton(icon=ft.icons.CAMERA_ALT, tooltip="Tomar con webcam", on_click=self.capture_photo_from_webcam)

        self.search_field = ft.TextField(
            label="Buscar usuario...",
            hint_text="Nombre, DNI, Email, Teléfono",
            prefix_icon=ft.icons.SEARCH,
            on_change=self.search_users,
            expand=True
        )

        self.selected_user_id = None
        self.user_list = ft.Column(spacing=10)

        self.page.add(
            ft.ResponsiveRow([
                ft.Container(
                    content=ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text("Formulario de Usuario", style=ft.TextThemeStyle.TITLE_MEDIUM),
                                self.name_field,
                                self.dni_field,
                                self.email_field,
                                self.phone_field,
                                ft.Row([
                                    self.photo_button,
                                    self.photo_button_web,
                                    self.photo_preview
                                ], alignment=ft.MainAxisAlignment.START),
                                ft.Row([
                                    ft.ElevatedButton("Crear", icon=ft.icons.ADD, on_click=self.create_user),
                                    ft.ElevatedButton("Actualizar", icon=ft.icons.SAVE, on_click=self.update_user),
                                ], alignment=ft.MainAxisAlignment.END)
                            ]),
                            padding=20
                        )
                    ),
                    col={"xs": 12, "md": 5}
                ),
                ft.Container(
                    content=ft.Column([
                        self.search_field,
                        ft.Text("Usuarios Registrados", style=ft.TextThemeStyle.TITLE_MEDIUM),
                        self.user_list
                    ]),
                    col={"xs": 12, "md": 7}
                )
            ])
        )

        self.refresh_user_list()

    # === Funcionalidad ===
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
        if not photo:
            photo = "utils/img/captura_centrada.png"
        
        if not validate_name(name):
            show_snackbar(self.page, message="El nombre es inválido")
            return
        if not validate_dni(dni):
            show_snackbar(self.page, "El DNI es inválido. Debe contener sólo números (8 dígitos).")
            return
        if not validate_email(email):
            show_snackbar(self.page, "El email es inválido. Ejemplo: usuario@gmail.com")
            return
        if not validate_phone(phone):
            show_snackbar(self.page, "El teléfono es inválido. Debe contener solo números (10 a 13 dígitos)")
            return
        
        self.controller.create_user(name, dni, email, phone, photo)
        self.clear_fields()
        self.refresh_user_list()
        show_snackbar(self.page, "Usuario creado correctamente", color=ft.colors.GREEN_400)
        
    def update_user(self, e):
        if self.selected_user_id:
            name = self.name_field.value
            dni = self.dni_field.value
            email = self.email_field.value
            phone = self.phone_field.value
            photo = self.photo_path
            
            if not validate_name(name):
                show_snackbar(self.page, message="El nombre es inválido")
                return
            if not validate_dni(dni):
                show_snackbar(self.page, "El DNI es inválido. Debe contener sólo números (8 dígitos).")
                return
            if not validate_email(email):
                show_snackbar(self.page, "El email es inválido. Ejemplo: usuario@gmail.com")
                return
            if not validate_phone(phone):
                show_snackbar(self.page, "El teléfono es inválido. Debe contener solo números (10 a 13 dígitos)")
                return
        
            self.controller.update_user(self.selected_user_id, name, dni, email, phone, photo)
            self.selected_user_id = None
            self.clear_fields()
            self.refresh_user_list()
            show_snackbar(self.page, "Usuario actualizado", color=ft.colors.BLUE_400)

    def delete_user(self, e, user_id):
        self.controller.delete_user(user_id)
        self.refresh_user_list()
        show_snackbar(self.page, "Usuario eliminado")

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
            user_card = ft.Card(
                content=ft.Container(
                    content=ft.Row([
                        ft.Image(src=user.photo or "", width=50, height=50, border_radius=5),
                        ft.Column([
                            ft.Text(f"{user.name}", weight="bold"),
                            ft.Text(f"DNI: {user.dni} | Email: {user.email} | Tel: {user.phone}", size=12),
                        ], expand=True),
                        ft.IconButton(icon=ft.icons.EDIT, tooltip="Editar", on_click=lambda e, u=user: self.select_user(e, u)),
                        ft.IconButton(icon=ft.icons.DELETE, tooltip="Eliminar", on_click=lambda e, uid=user.id: self.delete_user(e, uid)),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=10
                )
            )
            self.user_list.controls.append(user_card)
        if len(users)==0:
            self.user_list.controls.append(ft.Text("No hay usuarios registrados", style=ft.TextThemeStyle.BODY_MEDIUM))
            self.user_list.update()
            
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
        self.photo_path = "utils/img/captura_centrada.png"
        self.photo_preview.src = self.photo_path
        self.page.update()

    def capture_photo_from_webcam(self, e):
        photo_path = capture_face_photo()
        if photo_path:
            self.photo_path = photo_path
            self.photo_preview.src = photo_path
            self.page.update()
        else:
            show_snackbar(self.page, "No se capturó una imagen válida desde la webcam.")