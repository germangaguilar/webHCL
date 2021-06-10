# Generated by Django 3.2 on 2021-05-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Head_name', models.CharField(max_length=100)),
                ('No_of_adults', models.IntegerField()),
                ('no_of_children', models.IntegerField()),
                ('Identity_no', models.CharField(max_length=100)),
                ('Room_code', models.IntegerField()),
                ('No_of_nights', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roomtypecode', models.CharField(max_length=100)),
                ('Roomcode', models.IntegerField()),
                ('typename', models.TextField(max_length=100)),
                ('capacity', models.TextField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('Availible', models.BooleanField(default=True)),
            ],
        ),
    ]
