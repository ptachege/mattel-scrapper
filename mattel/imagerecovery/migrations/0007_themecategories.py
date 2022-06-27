# Generated by Django 3.2 on 2022-06-15 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagerecovery', '0006_lego'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_url', models.TextField(blank=True, max_length=20000, null=True)),
                ('crawled', models.BooleanField(default=False)),
            ],
        ),
    ]