from django.contrib import admin
from . models import Barang

# Register your models here.

class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg', 'nama', 'stok', 'harga', 'link_gbr')
    search_fields = ('nama',)

admin.site.register(Barang, BarangAdmin)