from django.db import transaction
from django.http import JsonResponse, HttpResponse

from shopping.models import Product
import json


def update_product(request):
    pass


@transaction.atomic()
def create_product(request):
    body = json.loads(request.body)
    # _name = body['name']
    _size = body['size']
    _price = body['price']
    _weight = body['weight']
    _image_url = body['image_url']
    _category = body['category']

    product = Product(size=_size, price=_price, weight=_weight, image_url=_image_url, category=_category)
    product.save()

    return HttpResponse('success')


# def create(request):
#     data = request.body
#     _weight = int(data.weight) * 100
#     p = Product(name=data.name, price=data.amount, size=data.size, weight=_weight)
#     p.save()
#     return JsonResponse({"data": {"name": p.name}})


def list_product(request):
    products = Product.objects.all()
    # json_result = serializers.serialize("json", list(products.values()))
    json_list = list(products.values())

    return JsonResponse({"data": json_list})
