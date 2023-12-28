from django.db import models
from django.db.models import Q
from check_constraint.models import AnnotatedCheckConstraint
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 30, null=False)
    email = models.EmailField(null=False, unique=True)
    mobile = models.CharField(max_length = 10, unique = True)
    city = models.CharField(max_length = 40)
    def __str__(self):
        return self.email
    
class Purchase(models.Model):
    product_name = models.CharField(max_length = 30, null=False)
    quantity = models.IntegerField(null = True)
    price = models.IntegerField(null = True)
    mrp = models.IntegerField(null = True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    def __str__(self):
        return self.product_name
    
    class Meta:
        constraints = [
            AnnotatedCheckConstraint(
                check=Q(price__lt=models.F('mrp')),
                name='%(app_label)s_%(class)s_price_check',
            )
        ]
class shipping_details(models.Model):
    address = models.CharField(max_length = 50,null = False)
    city = models.CharField(max_length = 30,null = False)
    pincode = models.CharField(max_length = 6,null = False)
  
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    
    
