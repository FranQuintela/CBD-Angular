from django.conf.urls import url
from rest_api.views import *
from rest_api.views import category
from rest_api.views import connectors
from rest_api.views import supplier

from django.urls import path
urlpatterns = [

    url(r'^api/products$', getAllProducts),
    url(r'^api/products/(?P<productID>[0-9]+)$', productDetails),
    url(r'^api/categories$', category.getAllCategories),
    url(r'^api/suppliers/(?P<supplierID>[0-9]+)$', supplier.supplierDetails),
    url(r'^api/suppliers$', supplier.getAllSuppliers),
    url(r'^api/categories/(?P<categoryID>[0-9]+)$', category.categoryDetails),
    url(r'^api/products/categories$', connectors.connectPaC),
    url(r'^api/products/suppliers$', connectors.connectPaS),

]