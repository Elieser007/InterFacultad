# Generated by Django 3.1.2 on 2020-10-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_auto_20201003_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
    ]
