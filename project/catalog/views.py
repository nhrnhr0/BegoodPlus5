from django.shortcuts import render

# Create your views here.
def catalog_page(request):
    ret = render(request, 'catalog.html',{})
    return ret