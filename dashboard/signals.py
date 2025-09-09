# signals.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, Company

@receiver(post_save, sender=User)
def create_user_profile_and_company(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        # Create a default company
        company = Company.objects.create(company_name=f"Default Company",company_address="Default")

        # Create profile linked to user and company
        UserProfile.objects.create(user=instance, company=company)
