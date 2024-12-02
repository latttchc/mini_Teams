from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from work.models import Member

@receiver(post_save, sender=User)
def create_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
