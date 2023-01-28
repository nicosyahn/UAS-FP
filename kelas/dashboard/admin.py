from django.contrib import admin

# Register your models here.
from .models import *

class kolomBarang(admin.ModelAdmin):
    list_display=['kodebrg', 'nama', 'stok', 'harga', 'link_gbr', 'jenis_id']
    search_fields=['kodebrg', 'nama']
    list_filter=('jenis_id',)
    list_per_page= 3

class kolomLevel(admin.ModelAdmin):
    list_display=['level', 'bonus']
    search_fields=['level']

class kolomStatus(admin.ModelAdmin):
    list_display=['status']
    search_fields=['status']

class kolomMembership(admin.ModelAdmin):
    list_display=['kodemem', 'nama', 'status', 'level_id']
    search_fields=['kodemem', 'nama']
    list_filter=('level_id',)
    list_per_page= 3


admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis)
admin.site.register(Membership, kolomMembership)
admin.site.register(Level, kolomLevel)
admin.site.register(Transaksi)
admin.site.register(Detailtrans)
admin.site.register(Status, kolomStatus)