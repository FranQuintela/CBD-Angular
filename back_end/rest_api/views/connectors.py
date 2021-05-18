from django.http import JsonResponse
from rest_api.models.models import Product
from rest_api.models.models import Category
from rest_api.models.models import Supplier

from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def connectPaC(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        productID = json_data['productID']
        categoryID = json_data['categoryID']
        try:
            product = Product.nodes.get(productID=productID)
            category = Category.nodes.get(categoryID=categoryID)

            res = product.categoryID.connect(category)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def connectPaS(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        productID = json_data['productID']
        supplierID = json_data['supplierID']
        try:
            product = Product.nodes.get(productID=productID)
            print(product)
            supplier = Supplier.nodes.get(supplierID=supplierID)
            print(supplier)

            res = product.supplierID.connect(supplier)
            print(res)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
