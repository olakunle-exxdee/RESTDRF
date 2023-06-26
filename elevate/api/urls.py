from django.urls import path

from . import views

urlpatterns = [
    path("products", views.product_lists, name="products"),
    path("products/<int:pk>/", views.single_product, name="single_product"),
]
