# Generated by Django 2.0.7 on 2018-07-18 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='register',
            unique_together={('name', 'description')},
        ),
    ]
