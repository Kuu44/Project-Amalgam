# Generated by Django 3.0.6 on 2020-08-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0005_auto_20200826_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.CharField(choices=[('1', 'Novel'), ('2', 'Course')], default=None, max_length=20),
        ),
    ]
