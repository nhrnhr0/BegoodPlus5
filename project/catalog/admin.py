from django.contrib import admin

# Register your models here.
from .models import CatalogAlbum, CatalogImage

from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableInlineAdminMixin

class CatalogImageTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    # We don't use the Button model but rather the juction model specified on Panel.
    model = CatalogAlbum.images.through


class CatalogAlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display =  ('title', 'slug',)
    inlines = (CatalogImageTabularInline,)
    pass
admin.site.register(CatalogAlbum, CatalogAlbumAdmin)

class CatalogImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display =  ('title',)
    pass
admin.site.register(CatalogImage, CatalogImageAdmin)