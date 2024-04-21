from django.shortcuts import render
from django.views import View
from .models import MenuItem

class MenuView(View):
    def get(self, request, menu_name):
        menu = MenuItem.objects.filter(name=menu_name)
        return render(request, 'menu.html', {'menu': menu})