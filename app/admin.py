from django.contrib import admin

from app.models import Hamkorlar, Visa, Dokument

# Register your models here.

@admin.register(Hamkorlar)
class HamkorAdmin(admin.ModelAdmin):
    list_display = ['id', 'hamkor_nomi']
    search_fields = ['hamkor_nomi']


@admin.register(Dokument)
class DokumentAdmin(admin.ModelAdmin):
    list_display = ['turistlar_soni', 'xujjat_nomi']
    search_fields = ['xujjat_nomi']
    prepopulated_fields = {'slug': ('xujjat_nomi',)}


# admin.site.register(Hamkorlar)
# admin.site.register(Dokument)
admin.site.register(Visa)

