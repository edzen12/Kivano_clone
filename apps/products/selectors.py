from apps.products.models import Product


def get_home_products(limit=12):
    # Товары для главной страницы
    return (
        Product.objects.active()
        .in_stock().with_related()
        .order_by('created_at')[:limit]
    )

def get_featured_products(limit=12):
    # Рекомендуемые товары 
    return (
        Product.objects.active()
        .featured()
        .in_stock()
        .with_related()
        .order_by('created_at')[:limit]
    )

def get_hit_products(limit=12):
    # Хиты продаж 
    return (
        Product.objects
        .active()
        .hits()
        .in_stock()
        .with_related()
        .order_by('created_at')[:limit]
    )

def get_new_products(limit=12):
    # Новинки
    return (
        Product.objects
        .active()
        .news()
        .in_stock()
        .with_related()
        .order_by('created_at')[:limit]
    )


def get_product_by_category(category):
    # Все товары категории
    return (
        Product.objects
        .active() 
        .in_stock()
        .with_related()
        .filter(category=category)
    )

def get_product_by_slug(slug):
    # Детальная страница товара
    return (
        Product.objects
        .active()  
        .with_related()
        .get(slug=slug)
    )