# Generated by Django 4.2.13 on 2024-05-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktable',
            name='date_and_time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]