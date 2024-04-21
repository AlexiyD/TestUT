from django import template
from TestUT.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.get(name=menu_name)
    return menu.render_menu()