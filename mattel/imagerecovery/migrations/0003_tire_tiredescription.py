# Generated by Django 3.2 on 2022-03-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagerecovery', '0002_tire'),
    ]

    operations = [
        migrations.AddField(
            model_name='tire',
            name='tiredescription',
            field=models.CharField(default=True, max_length=2000, null=True),
        ),
    ]