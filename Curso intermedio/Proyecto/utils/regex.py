import re

# Expresiones regulares comunes
NAME_REGEX = re.compile(r"^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,50}$")
DNI_REGEX = re.compile(r"^\d{7,10}$")  # acepta solo números (7 a 10 dígitos)
PHONE_REGEX = re.compile(r"^\+?\d{7,15}$")  # números con o sin prefijo internacional
EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

def validate_name(name: str) -> bool:
    return bool(NAME_REGEX.match(name))

def validate_dni(dni: str) -> bool:
    return bool(DNI_REGEX.match(dni))

def validate_phone(phone: str) -> bool:
    return bool(PHONE_REGEX.match(phone))

def validate_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))
