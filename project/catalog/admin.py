from django.contrib import admin

# Register your models here.
from .models import CatalogAlbum
from adminsortable2.admin import SortableAdminMixin

class CatalogAlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display =  ('title', 'slug',)
    pass
admin.site.register(CatalogAlbum, CatalogAlbumAdmin)