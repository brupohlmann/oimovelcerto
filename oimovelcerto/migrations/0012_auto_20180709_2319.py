# Generated by Django 2.0.7 on 2018-07-10 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oimovelcerto', '0011_auto_20180709_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='image',
            new_name='images',
        ),
    ]
