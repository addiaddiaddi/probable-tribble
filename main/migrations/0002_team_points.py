# Generated by Django 2.2.7 on 2021-01-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
