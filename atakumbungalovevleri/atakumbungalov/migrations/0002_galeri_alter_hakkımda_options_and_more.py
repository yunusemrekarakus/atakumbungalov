# Generated by Django 4.1.5 on 2023-02-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atakumbungalov', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='galeri')),
            ],
            options={
                'verbose_name': 'Galeri',
            },
        ),
        migrations.AlterModelOptions(
            name='hakkımda',
            options={'verbose_name': 'Hakkımda'},
        ),
        migrations.AlterModelOptions(
            name='hizmetler',
            options={'verbose_name': 'Hizmetler'},
        ),
    ]
