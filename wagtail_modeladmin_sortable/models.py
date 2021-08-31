from django.db import models


class AdminSortable(models.Model):
    sort_order = models.IntegerField(null=True, blank=True, editable=False)
    sortable_field = 'sort_order'

    class Meta:
        abstract = True
        ordering = ['sort_order']
