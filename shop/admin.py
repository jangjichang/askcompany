from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'desc', 'won_price', 'short_desc', 'is_publish']
    list_display_links = ['name']
    list_filter = ['is_publish', 'updated_at']
    search_fields = ['name']

    def won_price(self, item):
        won = str(item.price)
        comma_won = ""
        mod = len(won) % 3
        for i, v in enumerate(won):
            comma_won += v
            if (i+1) % 3 == mod and i != len(won)-1:
                comma_won += ","
        return comma_won

    def short_desc(self, item):
        return item.desc[:10]