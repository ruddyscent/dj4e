from django.contrib import admin
from unesco.models import Category, State, Iso, Region, Site

# Register your models here.
admin.site.register(Category)
admin.site.register(State)
admin.site.register(Iso)
admin.site.register(Region)
admin.site.register(Site)
