# Generated by Django 2.2.3 on 2019-07-31 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bit', '0005_auto_20190731_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('repeat_password', models.CharField(max_length=30)),
            ],
        ),
    ]
