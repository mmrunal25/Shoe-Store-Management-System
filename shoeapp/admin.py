from django.contrib import admin
from .models import Shoe, Cart, CartItems #CustomUser

#@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):   # check for this is not present it files
    list_display = ('id', 'brand', 'price', 'size', 'color')

# Register your models here.
#admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Cart)
admin.site.register(CartItems) 
#admin.site.register(CustomUser)


