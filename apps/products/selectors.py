from apps.products.models import Product


def get_active_products():
    return (
        Product.objects.filter(
            is_active=True
        ).select_related('category', 'brand')
    )


def get_product_by_slug(slug):
    return (
        Product.objects.select_related(
            'category', 'brand'
        ).prefetch_related('images').get(slug=slug)
    )