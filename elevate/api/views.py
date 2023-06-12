from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers
from rest_framework.decorators import api_view

# Create your views here.


def product_lists(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return render(request, "index.html", {"products": serializer.data})


@api_view(["GET", "POST"])
def product_list(request):
    pass

    if request.method == "GET":
        products = Product.objects.all()

        # serialized the product
        serializer = ProductSerializers(products, many=True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


@api_view(["GET", "P"])
def single_product(request, pk):
    pass

    if request.method == "GET":
        products = Product.objects.get(id=pk)

        # serialized the product
        serializer = ProductSerializers(products, many=False)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
