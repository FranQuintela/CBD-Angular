from django.http import JsonResponse
from rest_api.models.models import Product
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def getAllProducts(request):
    if request.method == 'GET':
        try:
            # products = Product.nodes.all()
            products = Product.nodes.filter(productID__lt="200")

            response = []
            for product in products :
                obj = {
                    "productID": product.productID,
                    "productName": product.productName,
                    "unitPrice": product.unitPrice,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one product
        json_data = json.loads(request.body)
        productID = json_data['productID']
        productName = json_data['productName']
        unitPrice = int(json_data['unitPrice'])
        try:
            product = Product(productID = productID, productName=productName, unitPrice=unitPrice)
            product.save()
            response = {
                "productID": product.productID,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def productDetails(request, productID):
    if request.method == 'GET':
        try:
            product = Product.nodes.get(productID=productID)
            print('get success')
            response = {
                "productID": product.productID,
                "productName": product.productName,
                "unitPrice": product.unitPrice,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one product
        json_data = json.loads(request.body)
        productName = json_data['productName']
        unitPrice = int(json_data['unitPrice'])
        try:
            product = Product.nodes.get(productID=productID)
            product.productName = productName
            product.unitPrice = unitPrice
            product.save()
            response = {
                "productID": product.productID,
                "productName": product.productName,
                "unitPrice": product.unitPrice,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one product
        json_data = json.loads(request.body)
        productID = json_data['productID']
        try:
            product = Product.nodes.get(productID=productID)
            product.delete()
            response = {"success": "Product deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)