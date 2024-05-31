from django.db import models
from django.utils.text import slugify
from category.models import Category
import uuid

def image_product_upload(instance,file_name:str):
    extension = file_name.split('.')[1]
    return f'products\{instance.name}.{extension}'



class Product(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField( max_length=250)
    slug = models.SlugField(unique=True,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to=image_product_upload, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products") 

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)


    def __str__(self):
        return self.name
