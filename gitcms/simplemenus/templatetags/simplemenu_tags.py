from django import template
register = template.Library()

from simplemenus.models import Menu

@register.inclusion_tag('simplemenus/menu.html')
def show_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    return { 'items' : menu.children }

