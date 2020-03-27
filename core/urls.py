from django.urls import path
from .views import item_list, checkout, products

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    path('checkout/', checkout, name="checkout"),
    path('products/', products, name="products")

]
