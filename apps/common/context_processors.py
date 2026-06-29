from apps.catalog.selectors import get_menu_categories


def menu_categories(request):
    # Категория главного меню
    return {
        'menu_categories': get_menu_categories()
    }