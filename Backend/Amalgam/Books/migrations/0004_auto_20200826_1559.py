# Generated by Django 3.0.6 on 2020-08-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_auto_20200826_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
