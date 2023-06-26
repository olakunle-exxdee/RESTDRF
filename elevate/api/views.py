from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

# Create your views here.


@api_view(["GET", "POST"])
def product_lists(request):
    pass

    if request.method == "GET":
        products = Product.objects.all()

        # serialized the product
        serializer = ProductSerializers(products, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        try:
            serializer = ProductSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except serializer.is_not_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def single_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # serialized the product
        serializer = ProductSerializers(product, many=False)
        return Response(serializer.data)
