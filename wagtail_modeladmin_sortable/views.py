from django.apps import apps
from django.db import transaction
from django.http.response import JsonResponse
from django.views.generic import FormView
from wagtail.contrib.modeladmin.views import IndexView

from .forms import SortingForm


class SortableIndexView(FormView, IndexView):
    """
    Index view overriding the base index
    admin view to add the sorting logic.
    """

    form_class = SortingForm

    def get_success_url(self):
        return self.index_url

    def form_valid(self, form):
        super(SortableIndexView, self).form_valid(form)

        if self.request.is_ajax():
            order_ids = self.request.POST.getlist("items[]")
            app_label = self.model_admin.model._meta.app_label
            model_label = self.model_admin.model.__name__

            if order_ids and app_label and model_label:
                model = apps.get_model(app_label, model_label)

                with transaction.atomic():
                    for order, pk in enumerate(order_ids):
                        model.objects.filter(pk=pk).update(sort_order=order)

                return JsonResponse(
                    {
                        "message": "Successfully ordered elements in database",
                    },
                    status=200,
                )

            return JsonResponse({"message": "Invalid Data"}, status=400)

        return JsonResponse({"message": "Invalid request source"}, status=400)
