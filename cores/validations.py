import re

from django.forms import ValidationError

EMAIL_REGEX    = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"
PASSWORD_REGEX = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+?&]{8,}$"

def validate_email(email):
    if not re.match(EMAIL_REGEX, email):
        raise ValidationError("INVALID_ERROR")

def validate_password(password):
    if not re.match(PASSWORD_REGEX, password):
        raise ValidationError("INVALID_ERROR")
