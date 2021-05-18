from django.db import models

from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, FloatProperty, BooleanProperty

# Create your models here.
class Category(StructuredNode):
    categoryID = UniqueIdProperty()

    description = StringProperty()
    categoryName = StringProperty()
    picture = StringProperty()

class Supplier(StructuredNode):
    supplierID = UniqueIdProperty()

    address = StringProperty()
    city = StringProperty()
    companyName = StringProperty()
    contactName = StringProperty()
    contactTitle = StringProperty()
    country = StringProperty()
    fax = StringProperty()
    homePage = StringProperty()
    phone = StringProperty()
    postalCode = StringProperty()
    region = StringProperty()
    

class Product(StructuredNode):
    productID = UniqueIdProperty()

    reorderLevel = IntegerProperty()
    unitsInStock = IntegerProperty()
    unitPrice = FloatProperty()
    supplierID = StringProperty()
    quantityPerUnit = StringProperty()
    discontinued = BooleanProperty()
    productName = StringProperty()
    unitsOnOrder = IntegerProperty()

#     # Relations :
    categoryID = RelationshipTo(Category, 'PART_OF')
    supplierID = RelationshipTo(Supplier, 'SUPPLIES')
#     friends = RelationshipTo('Person','FRIEND')




