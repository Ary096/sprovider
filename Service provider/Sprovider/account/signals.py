from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User, ProviderProfile, CustomerProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Only create profile when user is newly registered
        if instance.role == 'provider' and not hasattr(instance, 'provider_profile'):
            ProviderProfile.objects.create(user=instance)
        elif instance.role == 'customer' and not hasattr(instance, 'customer_profile'):
            CustomerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == 'provider' and hasattr(instance, 'provider_profile'):
        instance.provider_profile.save()
    elif instance.role == 'customer' and hasattr(instance, 'customer_profile'):
        instance.customer_profile.save()
