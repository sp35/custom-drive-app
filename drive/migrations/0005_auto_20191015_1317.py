# Generated by Django 2.2.4 on 2019-10-15 13:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drive', '0004_delete_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='Data',
        ),
    ]
