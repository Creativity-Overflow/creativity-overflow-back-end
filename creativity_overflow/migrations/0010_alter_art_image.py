# Generated by Django 4.1.5 on 2023-08-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativity_overflow', '0009_alter_art_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
