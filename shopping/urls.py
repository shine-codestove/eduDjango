from django.urls import path

from . import views

# /shopping/
urlpatterns = [
    path('product/list/', views.list_product, name='product_list'),
    path('product/create/', views.create_product, name='product_create'),
    path('product/update/', views.update_product, name='product_update'),
]
