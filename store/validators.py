from django.core.exceptions import ValidationError

def validate_eleven_digits(value):
    if not (10**10 <= value < 10**11):
        raise ValidationError('The number must have exactly 11 digits.')
