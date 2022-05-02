from django.db import models
from django.contrib.auth.models import User

# def get_name(self):
#     return f"{self.first_name} {self.last_name}"
#
# User.add_to_class("__str__", get_name)

class Address(models.Model):
    street = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

class Company(models.Model):
    status_choices = (
        ("N", "New"),
        ("L", "Lead"),
        ("O", "Opportunity"),
        ("C", "Active Customer"),
        ("FC", "Former Customer"),
        ("I", "Inactive")
    )

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=2, default="N", choices=status_choices)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    identification_number = models.CharField(max_length=100)
    address = models.ForeignKey("Address", on_delete=models.SET_NULL, null=True)

class Contact(models.Model):
    primary_company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class Opportunity(models.Model):
    status_choices = (
        ("1", "Prospecting"),
        ("2", "Analysis"),
        ("3", "Proposal"),
        ("4", "Negotiation"),
        ("5", "Closed Won"),
        ("0", "Closed Lost")
    )

    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    sales_manager = models.ForeignKey(User, on_delete=models.RESTRICT)
    primary_contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=2, default="1", choices=status_choices)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    office_number = models.CharField(max_length=10, blank=True, null=True)
    manager = models.ForeignKey("Employee", on_delete=models.SET_NULL, null=True, blank=True)

from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
from django.core.mail import send_mail
@receiver(post_save, sender=Opportunity)
def create_opportunity(sender, instance, created, **kwargs):
    if created:
        send_mail("Opporunity was created", instance.company.name, "test@mojefirma.cz", ["manazer@mojefirma.cz"])
