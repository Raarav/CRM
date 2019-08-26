from django.db import models

# Create your models here.

######### task model #############
class Task(models.Model):
    sub=models.CharField(max_length=2000)
    dis=models.CharField(max_length=100000)
    start_date=models.DateField()
    end_date=models.DateField()

    class Meta:
        _db_table='task'

######### end task model#############

########## Registraion model #############

class Register(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    repeat_password=models.CharField(max_length=30)

    class Meta:
        _db_table='register'

########## end Registraion model #############\

########## Invoice model #############

Size_product=(
    ('select','Select'),
    ('s','S'),
    ('m','M'),
    ('l','L'),
    ('xl','XL'),
    ('xxl','XXL'),
)

class MakeInvoiceModel(models.Model):
    OrderNumber=models.CharField(max_length=5000)
    InvoiceNumber=models.CharField(max_length=5000)
    ProductName=models.CharField(max_length=5000)
    ProductId=models.CharField(max_length=5000)
    Quality=models.CharField(max_length=5000)
    Price=models.CharField(max_length=5000)
    Size=models.CharField(max_length=6, choices=Size_product, default='select')
    UserFullName=models.CharField(max_length=5000)
    Email=models.EmailField()
    ContactNumber=models.CharField(max_length=5000)
    Address=models.CharField(max_length=5000)
    ShippingUserFullName=models.CharField(max_length=5000)
    ShippingUserContactNumber=models.CharField(max_length=5000)
    City=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    ZipCode=models.CharField(max_length=5000)
    ClientGst=models.CharField(max_length=2000)
    ModOfPayment=models.CharField(max_length=50)
    Date=models.DateField()
    ShippingCost=models.CharField(max_length=5000)


    class Meta:
        _db_table='invoicemodel'


########## end Invoice model #############


