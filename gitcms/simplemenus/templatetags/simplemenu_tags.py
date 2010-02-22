from django import template
register = template.Library()

from gitcms.simplemenus.models import Menu

@register.inclusion_tag('simplemenus/menu.html')
def show_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    return { 'items' : menu.children }

@register.inclusion_tag('simplemenus/tabs.html')
def show_tabs(menu_name):
    menu = Menu.objects.get(name=menu_name)
    items = menu.children
    for it in items:
        it.active = False
    return { 'items' : items }
