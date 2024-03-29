from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Create your models here.
'''class CustomUser(AbstractUser):
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)'''

class Shoe(models.Model):
    id = models.AutoField(primary_key = True)
    brand = models.CharField(max_length = 50)
    price = models.IntegerField()
    size = models.IntegerField()
    color = models.CharField(max_length = 50)
    product_image = models.ImageField(upload_to='product_images/', null = True, blank = True)
    
       #bio = models.FileField(upload_to='bio/', null = True, blank = True)
    
    def __str__(self):
       return f"{self.id} {self.brand} {self.price} {self.size} {self.color} {self.product_image}"

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return f'{self.user.username}'
    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{ self.quantity }'
    