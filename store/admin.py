from django.contrib import admin
from store.models import Mattress

# Register your models here.

class MattressAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'width', 'height')
admin.site.register(Mattress, MattressAdmin)
