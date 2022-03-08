from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from user.models import UserProfile, WishList

from .serializers import ProductSerializer, WishListSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.


class CreateProduct(CreateAPIView):
    permission_classes = ([IsAuthenticated])
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    
class ListProducts(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
class WishListLists(ListAPIView):
    permission_classes = ([IsAuthenticated])
    serializer_class = WishListSerializer
    
    def get_queryset(self):
        user = self.request.user
        userprof = UserProfile.objects.get(user = user)
        wishListObj = WishList.objects.get(userProfile_id = userprof.id)
        return wishListObj.product_set.all()
    




