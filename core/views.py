from django.db.models import Count
from django.shortcuts import redirect
from django.views.generic import ListView, View
from core.constants import TOP_MILLIONAIRES_COUNT
from core.models import Millionaire, VoteMillionaire


class MillionaireListView(ListView):
    model = Millionaire
    paginate_by = 16
    template_name = 'core/index.html'

    def get_queryset(self):
        return self.model.objects.prefetch_related('country', 'company', 'votes')


millionaire_list_view = MillionaireListView.as_view()


class MillionaireVoteCreateView(View):
    def get(self, request, millionaire_id, *args, **kwargs):
        VoteMillionaire.objects.create(millionaire_id=millionaire_id)
        return redirect('core:millionaire_list_url')


millionaire_vote_create_view = MillionaireVoteCreateView.as_view()


class TopMillionairesIndexView(ListView):
    model = Millionaire
    template_name = 'core/index.html'

    def get_queryset(self):
        top_millionaires = self.model.objects.prefetch_related('country', 'company', 'votes')\
            .annotate(votes_count=Count('votes')).order_by('-votes_count')[:TOP_MILLIONAIRES_COUNT]
        return top_millionaires[:TOP_MILLIONAIRES_COUNT]


top_millionaires_index_view = TopMillionairesIndexView.as_view()
