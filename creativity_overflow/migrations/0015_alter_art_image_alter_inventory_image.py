# Generated by Django 4.1.5 on 2023-08-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativity_overflow', '0014_alter_art_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='image',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]
