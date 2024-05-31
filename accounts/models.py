from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
# Create your models here.


def uplad_user_image(instance , file_name):
    extension = file_name.split('.')[1]
    return f'user/{instance.user}.{extension}'



class Account(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=uplad_user_image, height_field=None, width_field=None, max_length=None , null=True, blank=True)
    phone = models.CharField(max_length=50)


    class Meta:
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    def __str__(self):
        return str(self.user)
    
    @receiver(post_save , sender=User)
    def create_user_account(sender , instance , created , **kwargs):
        if created:
            Account.objects.create(user=instance)
