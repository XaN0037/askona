# Generated by Django 4.1.6 on 2023-02-10 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0013_like_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Maqsad',
            new_name='maqsad',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Xususiyatlari',
            new_name='xususiyatlari',
        ),
    ]