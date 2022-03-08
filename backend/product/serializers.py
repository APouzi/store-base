
from rest_framework import serializers

from .models import WishList, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "inv_num", "wishlist_of"]

    def create(self, validated_data):
        return super().create(validated_data)
    

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']