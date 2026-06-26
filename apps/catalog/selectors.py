# Selector - место где лежат запросы к БД
from mptt.templatetags.mptt_tags import cache_tree_children
from apps.catalog.models import Category


def get_root_categories():
    # ТОлько верхние категории
    return Category.objects.root_nodes()


def get_menu_categories():
    # Полное дерево категории для меню
    categories = Category.objects.filter(is_active=True)
    return cache_tree_children(categories)