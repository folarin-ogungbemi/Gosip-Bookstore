from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining user
    delivery information and order history
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    user_phone_number = models.CharField(
        max_length=17, null=True, blank=True)
    user_address_line_1 = models.CharField(
        max_length=254, null=True, blank=True)
    user_address_line_2 = models.CharField(
        max_length=254, null=True, blank=True)
    user_zip = models.CharField(
        max_length=10, null=True, blank=True)
    user_city = models.CharField(
        max_length=100, null=True, blank=True)
    user_state = models.CharField(
        max_length=100,  null=True, blank=True)
    user_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the users profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
