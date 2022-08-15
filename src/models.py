from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

alphabetical_validator = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetical characters are allowed.')

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20, blank=False, validators=[alphabetical_validator])
    last_name = models.CharField(max_length=20, blank=True, validators=[alphabetical_validator])
    email = models.EmailField(max_length=30, blank=False, unique=True, validators=[EmailValidator])
    phone = PhoneNumberField(blank=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "users"
