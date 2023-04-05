from django.contrib import admin

# Register your models here.
from food.models import Item,Category

from django.contrib.admin  import AdminSite


class EventAdminSite(AdminSite):
    site_header = "FOOD ADMIN"
    site_title =  "FOOD ADMIN PORTAL"
    index_title = "Welcome to food"


event_food_admin = EventAdminSite(name='food_admin')



event_food_admin.register(Item)
event_food_admin.register(Category)