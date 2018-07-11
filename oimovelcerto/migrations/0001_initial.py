# Generated by Django 2.0.7 on 2018-07-10 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Titulo')),
                ('region', models.CharField(max_length=20, verbose_name='Região')),
                ('zipcode', models.CharField(max_length=9, verbose_name='CEP')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor')),
                ('description', models.CharField(max_length=200, verbose_name='Descrição')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Foto 2')),
            ],
        ),
    ]
