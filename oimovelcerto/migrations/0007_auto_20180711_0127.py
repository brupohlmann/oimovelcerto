# Generated by Django 2.0.7 on 2018-07-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oimovelcerto', '0006_auto_20180711_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/', verbose_name='Foto'),
        ),
    ]
