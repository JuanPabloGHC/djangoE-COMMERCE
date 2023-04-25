from django.shortcuts import render
from django.views import View

from products.models import Product

# Create your views here.
class Home(View):
    def get(self, request):
        productos = Product.objects.all()
        context = {
            'products': productos
        }
        return render(request, 'index.html', context)
