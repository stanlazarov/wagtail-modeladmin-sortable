from .views import SortableIndexView


class ModelAdminSortableMixin:
    index_view_extra_js = [
        'js/jquery-1.12.4.min.js',
        'js/jquery-ui.min.js',
        'js/sortable.js',
    ]
    index_view_extra_css = ['css/style.css']
    index_template_name = 'admin_sortable/index.html'
    index_view_class = SortableIndexView
    ordering = ('sort_order',)
    admin_sortable = True

    def get_index_view_extra_css(self):
        css = super().get_index_view_extra_css()
        return css + self.index_view_extra_css

    def get_index_view_extra_js(self):
        js = super().get_index_view_extra_js()
        return js + self.index_view_extra_js
