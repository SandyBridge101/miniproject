from django.db import models

# Create your models here.

class Category(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)

    def __str__(self) -> str: 
        return str(self.id)+' : '+str(self.name)
    
class Region(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)

    def __str__(self) -> str: 
        return str(self.id)+' : '+str(self.name)

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    price=models.DecimalField(decimal_places=2,max_digits=11,default=0)
    stock_quantity=models.IntegerField(default=0)
    category_id= models.ForeignKey(Category, on_delete=models.CASCADE)
    region_id= models.ForeignKey(Region, on_delete=models.CASCADE)
    image=models.CharField(max_length=10000,default='https://img.freepik.com/free-vector/shopping-cart-realistic_1284-6011.jpg?size=338&ext=jpg&ga=GA1.1.1141335507.1718064000&semt=ais_user')

    def __str__(self) -> str: 
        return str(self.id)+' : '+str(self.name)
    
class Cart(models.Model):
    id=models.IntegerField(primary_key=True)
    product_id=models.ManyToManyField(Product, related_name='products')
    quantity=models.IntegerField(default=0)

    def __str__(self) -> str: 
        return str(self.id)+' : '+str(self.quantity)