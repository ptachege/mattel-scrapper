# Generated by Django 3.2 on 2022-06-27 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerecovery', '0014_hasbrotoys'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hasbrotoys',
            old_name='age',
            new_name='whats_in_box',
        ),
    ]