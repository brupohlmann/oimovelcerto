# Generated by Django 2.0.7 on 2018-07-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oimovelcerto', '0007_auto_20180711_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='register',
            name='region',
            field=models.CharField(max_length=20, verbose_name='Bairro'),
        ),
    ]
