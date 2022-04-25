from django.views.generic import ListView
from core.models import Millionaire


class MillionaireListView(ListView):
    model = Millionaire
    paginate_by = 16
    template_name = 'core/index.html'

    def get_queryset(self):
        return self.model.objects.select_related('country', 'company')


millionaire_list_view = MillionaireListView.as_view()
