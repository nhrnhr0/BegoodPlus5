from django.shortcuts import render
from .models import CatalogAlbum
# Create your views here.
def catalog_page(request):
    albums = CatalogAlbum.objects.prefetch_related('images')
    context = {'albums':albums}
    ret = render(request, 'catalog.html',context=context)
    return ret