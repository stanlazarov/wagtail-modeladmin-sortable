# wagtail-modeladmin-sortable

Generic drag-and-drop ordering for objects in the Wagtail admin interface

Quick start
-----------

Install **wagtail_modeladmin_sortable**

```bash
$ pip install wagtail-modeladmin-sortable

```    

Add ``wagtail_modeladmin_sortable`` to ``INSTALLED_APPS`` the settings of your Django project:

```python
INSTALLED_APPS = [
  ...
  'wagtail_modeladmin_sortable',
]
```

Integrate your models
-----------

```python
from django.db import models
from wagtail_modeladmin_sortable.models import AdminSortable


class Example(AdminSortable):
    title = models.CharField('Title', max_length=255, null=True, blank=True)

    class Meta(AdminSortable.Meta):
        verbose_name = "Example"
        verbose_name_plural = "Examples"
```


#### In wagtail_hooks.py, add a mixin class to augment the functionality for sorting (be sure to put the mixin class before ModelAdmin):

```python
from wagtail.contrib.modeladmin.options import ModelAdmin
from wagtail_modeladmin_sortable.mixins import ModelAdminSortableMixin


class ExampleAdmin(ModelAdminSortableMixin, ModelAdmin):
    pass
```

##### License

Copyright &copy; 2021 Stanislav Lazarov.

MIT licensed.