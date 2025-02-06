from django.contrib import admin
from htmlcss.models import Laptop

# Register your models here.
class laptopadmin(admin.ModelAdmin):
    list_display=('name','link','price')

admin.site.register(Laptop,laptopadmin)