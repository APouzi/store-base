from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from user.models import UserProfile, WishList

from .serializers import ProductSerializer, WishListSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


# Create your views here.


class CreateProduct(CreateAPIView):
    permission_classes = ([IsAuthenticated])
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    
class ListProducts(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class EndUserProductWishList(RetrieveUpdateDestroyAPIView):
    permission_classes = ([IsAuthenticated])
    serializer_class = WishListSerializer

    def get_object(self):
        userProf = UserProfile.objects.get(user = self.request.user)
        instanceWishList = WishList.objects.get(userProfile = userProf)
        return instanceWishList

# PUT method, for creating an assoction realtionship
# url is store in the kwargs.
    def update(self, request, *args, **kwargs):
        # data = request.data
        # prodId = data['product_id']
        # productAdd = Product.objects.get(prodId)
        # # Pretty sure this is the wishlist, needs testing.
        data = request.data
        wishlistInstance = self.get_object()
        wishlistInstance.products.add(data['product_id'])
        serializer = WishListSerializer(wishlistInstance)
        return Response(serializer.data)

       
# The dissociation of the product from list
    def delete(self, request, *args, **kwargs):
        data = request.data
        wishlistInstance = self.get_object()
        wishlistInstance.products.remove(data['product_id'])
        serializer = WishListSerializer(wishlistInstance)
        return Response(serializer.data)









