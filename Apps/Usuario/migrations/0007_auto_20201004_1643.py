# Generated by Django 3.1.2 on 2020-10-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0006_auto_20201004_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]