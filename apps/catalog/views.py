from django.views.generic import TemplateView
from apps.catalog.selectors import get_menu_categories


class CategoryMenuView(TemplateView):
    template_name = 'catalog/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = get_menu_categories()
        return context
