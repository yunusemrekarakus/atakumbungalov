# Generated by Django 4.1.5 on 2023-02-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='ad_soyad',
            new_name='adsoyad',
        ),
    ]
