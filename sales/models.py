from django.db import models


class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)  
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Customers'


class Product(models.Model):
    productid = models.AutoField(db_column='ProductID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    category = models.CharField(db_column='Category', max_length=50, blank=True, null=True)
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Products'


class Order(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)
    customerid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerID')
    productid = models.ForeignKey(Product, models.CASCADE, db_column='ProductID')
    orderdate = models.DateField(db_column='OrderDate')
    quantity = models.IntegerField(db_column='Quantity')
    totalprice = models.DecimalField(db_column='TotalPrice', max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Orders'
