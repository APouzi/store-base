from django.urls import path
from .views import CreateProduct, WishListLists

urlpatterns = [
    path('create-product/', CreateProduct.as_view(), name = "create_product"),
    path('wishlist/', WishListLists.as_view(), name = "create_product"),
]