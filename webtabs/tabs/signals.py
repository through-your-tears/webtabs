from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import WebTag


@receiver(post_save, sender=WebTag)
def update_collection_datetime(sender, instance, created, **kwargs):
    if created and instance.collection:
        instance.collection.modified_at = timezone.now()
        instance.collection.save()
