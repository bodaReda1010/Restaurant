# Generated by Django 4.2.13 on 2024-05-28 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_remove_account_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
