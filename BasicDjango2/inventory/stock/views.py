from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


# Create your views here.


def index(request):
    #html = "<html><body>Home</body></html>"
    # return HttpResponse(html)
    product = Product.objects.all()
    return render(request, 'frontend/index.html', {'product': product})


def about(request):
    #html = "<html><body>Home</body></html>"
    # return HttpResponse(html)
    return render(request, 'frontend/about.html')


def contact(request):
    #html = "<html><body>Home</body></html>"
    # return HttpResponse(html)
    return render(request, 'frontend/contact.html')
