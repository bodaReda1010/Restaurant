from django.db import models
import uuid


def upload_chef_image(instance , file_name):
    extension = file_name.split('.')[1]
    return f'chef/{instance.name}.{extension}'


class Chef(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_chef_image, height_field=None, width_field=None, max_length=None)


    class Meta:
        verbose_name = ("Chef")
        verbose_name_plural = ("Chefs")

    def __str__(self):
        return self.name

