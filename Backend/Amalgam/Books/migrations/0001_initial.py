# Generated by Django 3.0.6 on 2020-08-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=40)),
                ('book_name', models.CharField(max_length=50)),
                ('date_time', models.DateField(auto_now_add=True)),
                ('original_price', models.IntegerField()),
                ('offered_price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=None)),
            ],
            options={
                'ordering': ['book_name'],
            },
        ),
    ]
