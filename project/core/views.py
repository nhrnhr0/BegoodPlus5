from django.shortcuts import render

# Create your views here.


def home_page(request):
    ret = render(request, 'home.html',{})
    return ret

