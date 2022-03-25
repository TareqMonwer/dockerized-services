from django.views.generic import ListView
from core.models import Millionaire


class MillionaireListView(ListView):
    model = Millionaire
    paginate_by = 16
    template_name = 'core/index.html'


millionaire_list_view = MillionaireListView.as_view()
