from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Profile, ShoppingCart, Favourite
from orders.models import Order, OrderLine, OrderStatus
from products.models import Clothes, Category, Variation, VariationOption, ClothingItem, ClothingConfiguration, Inventory


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(Profile)
admin.site.register(ShoppingCart)
admin.site.register(Favourite)

admin.site.register(Clothes)
admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(VariationOption)
admin.site.register(ClothingItem)
admin.site.register(ClothingConfiguration)
admin.site.register(Inventory)

admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(OrderStatus)