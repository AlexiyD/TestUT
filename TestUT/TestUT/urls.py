from django.contrib import admin
from django.urls import path
from TestUT.views import MenuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/<str:menu_name>/', MenuView.as_view(), name='menu'),
]