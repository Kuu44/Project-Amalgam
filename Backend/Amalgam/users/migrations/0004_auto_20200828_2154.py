# Generated by Django 3.0.6 on 2020-08-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200828_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
