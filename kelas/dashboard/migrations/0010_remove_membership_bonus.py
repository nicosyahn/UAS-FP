# Generated by Django 4.1.5 on 2023-01-17 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_membership_bonus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='bonus',
        ),
    ]
