from django.http import JsonResponse
from rest_api.models.models import Supplier
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def getAllSuppliers(request):
    if request.method == 'GET':
        try:
            suppliers = Supplier.nodes.all()
            response = []
            for supplier in suppliers :
                obj = {
                    "supplierID": supplier.supplierID,
                    "contactName": supplier.contactName,
                    "companyName": supplier.companyName,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one supplier
        json_data = json.loads(request.body)
        supplierID = json_data['supplierID']
        contactName = json_data['contactName']
        companyName = json_data['companyName']
        try:
            supplier = Supplier(supplierID = supplierID, contactName=contactName, companyName=companyName)
            supplier.save()
            response = {
                "supplierID": supplier.supplierID,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def supplierDetails(request, supplierID):
    if request.method == 'GET':
        try:
            supplier = Supplier.nodes.get(supplierID=supplierID)
            print('get success')
            response = {
                "supplierID": supplier.supplierID,
                "contactName": supplier.contactName,
                "companyName": supplier.companyName,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one supplier
        json_data = json.loads(request.body)
        contactName = json_data['contactName']
        companyName = json_data['companyName']
        try:
            supplier = Supplier.nodes.get(supplierID=supplierID)
            supplier.contactName = contactName
            supplier.companyName = companyName
            supplier.save()
            response = {
                "supplierID": supplier.supplierID,
                "contactName": supplier.contactName,
                "companyName": supplier.companyName,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one supplier
        # json_data = json.loads(request.body)
        # supplierID = json_data['supplierID']
        try:
            supplier = Supplier.nodes.get(supplierID=supplierID)
            supplier.delete()
            response = {"success": "Supplier deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)