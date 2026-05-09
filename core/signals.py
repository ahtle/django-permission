from django.db.models.signals import post_migrate 
from django.dispatch import receiver

from core.services import AuthService


@receiver(post_migrate)
def sync_auth_permissions(sender, **kwargs): 
    if sender.name != "core": 
        return

    return AuthService.sync_permissions()