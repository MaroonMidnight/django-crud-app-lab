from django.contrib import admin

from .models import Pokemon, Feeding, Item

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Feeding)
admin.site.register(Item)
