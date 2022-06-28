from django.db import transaction
from django.http import JsonResponse, HttpResponse

from shopping.models import Product
import json


def delete_product(request):
    product_id = request.GET.get('id')
    p = Product.objects.get(id=product_id)
    p.is_active = False

    p.save()

    return HttpResponse('delete success')


def update_product(request):
    product_id = request.GET.get('id')
    p = Product.objects.get(id=product_id)
    _data = json.loads(request.body)
    p.size = _data['size']
    p.price = _data['price']
    p.save()
    return HttpResponse('update success')


@transaction.atomic()
def create_product(request):
    body = json.loads(request.body)
    _name = body['name']
    _size = body['size']
    _price = body['price']
    _weight = body['weight']
    _image_url = body['image_url']
    _category = body['category']

    product = Product(name=_name, size=_size, price=_price, weight=_weight, image_url=_image_url, category=_category)
    product.save()

    return HttpResponse('success')


def list_product(request):
    products = Product.objects.all()
    # json_result = serializers.serialize("json", list(products.values()))
    json_list = list(products.values())

    return JsonResponse({"data": json_list})
