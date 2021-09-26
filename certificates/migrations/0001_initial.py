# Generated by Django 2.1 on 2020-05-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='images')),
                ('company', models.CharField(max_length=200)),
                ('show', models.BooleanField(default=False)),
            ],
        ),
    ]
