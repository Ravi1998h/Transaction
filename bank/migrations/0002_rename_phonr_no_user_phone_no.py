# Generated by Django 3.2.3 on 2021-07-23 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phonr_no',
            new_name='phone_no',
        ),
    ]
