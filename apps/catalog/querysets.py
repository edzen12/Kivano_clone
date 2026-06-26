from django.db import models
from mptt.templatetags.mptt_tags import cache_tree_children


class CategoryQuerySet(models.QuerySet):

    def active(self):
        return self.filter(is_active=True)
    
    def menu(self):
        return cache_tree_children(
            self.active()
        )