# Generated by Django 2.0.7 on 2018-07-18 18:30

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
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'register',
            },
        ),
    ]
