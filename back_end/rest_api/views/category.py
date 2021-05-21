from django.http import JsonResponse
from rest_api.models.models import Category
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def getAllCategories(request):
    if request.method == 'GET':
        try:
            categorys = Category.nodes.all()
            response = []
            for category in categorys :
                obj = {
                    "categoryID": category.categoryID,
                    "categoryName": category.categoryName,
                    "description": category.description,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one category
        json_data = json.loads(request.body)
        categoryID = json_data['categoryID']
        categoryName = json_data['categoryName']
        description = json_data['description']
        try:
            category = Category(categoryID = categoryID, categoryName=categoryName, description=description)
            category.save()
            response = {
                "categoryID": category.categoryID,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def categoryDetails(request, categoryID):
    if request.method == 'GET':
        try:
            category = Category.nodes.get(categoryID=categoryID)
            print('get success')
            response = {
                "categoryID": category.categoryID,
                "categoryName": category.categoryName,
                "description": category.description,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one category
        json_data = json.loads(request.body)
        categoryName = json_data['categoryName']
        description = json_data['description']
        try:
            category = Category.nodes.get(categoryID=categoryID)
            category.categoryName = categoryName
            category.description = description
            category.save()
            response = {
                "categoryID": category.categoryID,
                "categoryName": category.categoryName,
                "description": category.description,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one category
        # json_data = json.loads(request.body)
        # categoryID = json_data['categoryID']
        try:
            category = Category.nodes.get(categoryID=categoryID)
            category.delete()
            response = {"success": "Category deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)