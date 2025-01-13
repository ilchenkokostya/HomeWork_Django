from django.contrib import admin
from .models import *


# Register your models here.

# admin.site.register(Game, GameAdmin)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ['size', 'cost']
    list_display = ['title', 'cost', 'size']
    search_fields = ['title']
    list_editable = ['cost', 'size']
    ordering = ['title']
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ['balance', 'age']
    list_display = ['name', 'balance', 'age']
    search_fields = ['name']
    list_editable = ['age']
    readonly_fields = ['balance']
    ordering = ['name']
    list_per_page = 30


# admin.site.register(Buyer, BuyerAdmin)
# admin.site.register(Game, GameAdmin)
