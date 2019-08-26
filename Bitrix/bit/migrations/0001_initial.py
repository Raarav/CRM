# Generated by Django 2.2.3 on 2019-08-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MakeInvoiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderNumber', models.CharField(max_length=5000)),
                ('InvoiceNumber', models.CharField(max_length=5000)),
                ('ProductName', models.CharField(max_length=5000)),
                ('ProductId', models.CharField(max_length=5000)),
                ('Quality', models.CharField(max_length=5000)),
                ('Price', models.CharField(max_length=5000)),
                ('Size', models.CharField(choices=[('select', 'Select'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], default='select', max_length=6)),
                ('UserFullName', models.CharField(max_length=5000)),
                ('Email', models.EmailField(max_length=254)),
                ('ContactNumber', models.CharField(max_length=5000)),
                ('Address', models.CharField(max_length=5000)),
                ('ShippingUserFullName', models.CharField(max_length=5000)),
                ('ShippingUserContactNumber', models.CharField(max_length=5000)),
                ('City', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('ZipCode', models.CharField(max_length=5000)),
                ('ClientGst', models.CharField(max_length=2000)),
                ('ModOfPayment', models.CharField(max_length=50)),
                ('Date', models.DateField()),
                ('ShippingCost', models.CharField(max_length=5000)),
            ],
        ),
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
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=2000)),
                ('dis', models.CharField(max_length=100000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
