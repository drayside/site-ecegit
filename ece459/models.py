from django.db.models.signals import post_save, pre_delete

from django_ssh.models import Key

from ece459.utils import receive_key_create, receive_key_delete

# Signals
post_save.connect(receive_key_create, Key)
pre_delete.connect(receive_key_delete, Key)
