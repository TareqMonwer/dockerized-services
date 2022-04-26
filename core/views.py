from django.shortcuts import redirect
from django.views.generic import ListView, View
from core.models import Millionaire, VoteMillionaire


class MillionaireListView(ListView):
    model = Millionaire
    paginate_by = 16
    template_name = 'core/index.html'

    def get_queryset(self):
        return self.model.objects.select_related('country', 'company')


millionaire_list_view = MillionaireListView.as_view()


class MillionaireVoteCreateView(View):
    def get(self, request, millionaire_id, *args, **kwargs):
        VoteMillionaire.objects.create(millionaire_id=millionaire_id)
        return redirect('core:millionaire_list_url')


millionaire_vote_create_view = MillionaireVoteCreateView.as_view()
