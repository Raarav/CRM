# Generated by Django 2.2.3 on 2019-08-05 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bit', '0007_invoicemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicemodel',
            old_name='ShippingUserName',
            new_name='ShippingUserFullName',
        ),
    ]