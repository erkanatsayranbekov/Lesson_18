from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
