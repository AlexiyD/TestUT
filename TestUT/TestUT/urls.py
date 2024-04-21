from django.contrib import admin
from django.urls import path
from TestUT.views import MenuView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('menu/<str:menu_name>/', MenuView.as_view(), name='menu'),
]