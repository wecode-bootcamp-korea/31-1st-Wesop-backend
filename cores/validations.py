import re

from django.forms import ValidationError

regex_email             = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"
regex_password          = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+?&]{8,}$"

def email_validation(email):
    if not re.match(regex_email, email):
        raise ValidationError("INVALID_ERROR")

def password_validation(password):
    if not re.match(regex_password, password):
        raise ValidationError("INVALID_ERROR")
