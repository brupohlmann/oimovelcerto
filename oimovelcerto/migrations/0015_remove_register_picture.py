# Generated by Django 2.0.7 on 2018-07-10 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oimovelcerto', '0014_auto_20180709_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='picture',
        ),
    ]