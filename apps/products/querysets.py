from django.db import models


class ProductQuerySet(models.QuerySet):
    
    def active(self):
        return self.filter(is_active=True)

    def featured(self):
        return self.filter(is_featured=True)
    
    def hits(self):
        return self.filter(is_hit=True)
    
    def news(self):
        return self.filter(is_new=True)
    
    def with_related(self):
        return self.select_related(
            'category', 'brand'
        ).prefetch_related('images',)