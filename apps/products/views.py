from django.views.generic import TemplateView
from apps.products.selectors import (
    get_home_products,
    get_featured_products,
    get_hit_products,
    get_new_products
)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products']=get_home_products()
        context['featured_products']=get_featured_products()
        context['hit_products']=get_hit_products()
        context['new_products']=get_new_products()
        return context