from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        products_serializer = ProductSerializer(data=request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response(products_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', products_serializer.errors)
            return Response(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
