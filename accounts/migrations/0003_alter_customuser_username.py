# Generated by Django 4.0.4 on 2022-05-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]