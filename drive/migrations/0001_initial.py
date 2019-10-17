# Generated by Django 2.2.4 on 2019-10-15 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='data/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ManyToManyField(to='drive.File')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_user', to='drive.File')),
            ],
        ),
    ]
