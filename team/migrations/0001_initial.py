# Generated by Django 4.2.13 on 2024-05-23 09:49

from django.db import migrations, models
import team.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=team.models.upload_chef_image)),
            ],
            options={
                'verbose_name': 'Chef',
                'verbose_name_plural': 'Chefs',
            },
        ),
    ]