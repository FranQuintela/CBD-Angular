from django.http import JsonResponse
from rest_api.models.models import Product
from rest_api.models.models import Category

from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def connectPaC(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        productID = json_data['productID']
        categoryID = json_data['categoryID']
        try:
            print('get try')
            product = Product.nodes.get(productID="1")
            print("not found product")
            category = Category.nodes.get(categoryID="1")
            print("not found category")

            res = product.categoryID.connect(category)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
