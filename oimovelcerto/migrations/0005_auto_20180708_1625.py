# Generated by Django 2.0.7 on 2018-07-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oimovelcerto', '0004_auto_20180708_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='photo',
            field=models.ImageField(upload_to='media/', verbose_name='Foto'),
        ),
    ]