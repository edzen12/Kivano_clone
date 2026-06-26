from apps.catalog.models import Category


def get_menu_categories():
    # Категории для главного меню
    return (Category.objects.menu())

def get_root_categories():
    # Только родительские категории
    return (
        Category.objects.active().root_nodes()
    )

def get_category_by_slug(slug):
    return (Category.objects.active().get(slug=slug))