from django.shortcuts import render
from django.views.generic import View
from .models import MenuItem

class MenuView(View):
    def get(self, request, menu_name):
        menu = MenuItem.objects.get(name=menu_name)
        return render(request, 'menu.html', {'menu': menu})

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')