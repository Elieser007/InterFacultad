# Generated by Django 3.1.2 on 2020-10-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='miniatura',
            field=models.URLField(default=1, verbose_name='Imagen Miniatura'),
            preserve_default=False,
        ),
    ]
