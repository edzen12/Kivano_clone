from django.urls import path
from apps.catalog.views import CategoryMenuView

urlpatterns = [
    path(
        'categories', CategoryMenuView.as_view(), 
        name='categories'
    ),
]
