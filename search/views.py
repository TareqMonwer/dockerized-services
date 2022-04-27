from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.views.generic import View
from django.shortcuts import render
from django.contrib.postgres.search import (SearchVector, SearchRank, SearchHeadline,
                                            SearchQuery, TrigramSimilarity)
from core.models import Millionaire


class SearchMillionaires(View):
    paginate_by = 16

    def get_search_result_queryset(self, search_string):
        if search_string:
            vector = SearchVector('name', weight='A') + \
                SearchVector('profession', weight='B')
            search_query = SearchQuery(search_string)
            rank = SearchRank(vector, search_query)
            similarity = TrigramSimilarity('name', search_string)
            name_headline = SearchHeadline(
                'name',
                search_query,
                start_sel='<b><u><i>',
                stop_sel='</i></u></b>',
            )
            profession_headline = SearchHeadline(
                'profession',
                search_query,
                start_sel='<span class="bg-warning">',
                stop_sel='</span>',
            )
            results = Millionaire.objects.prefetch_related('country', 'company', 'votes') \
                .annotate(search=vector, rank=rank, similarity=similarity, total=rank+similarity,
                    name_headline=name_headline, profession_headline=profession_headline) \
                        .order_by('-total').filter(Q(similarity__gt=0.2) | Q(rank__gt=0.1))
            return results
        return []

    def get(self, request):
        search_string = request.GET.get('q')
        search_string = search_string if search_string else None
        results = self.get_search_result_queryset(search_string)
        rank = None

        paginator = Paginator(results, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        context = {
            'query': search_string,
            'rank': rank,
            'results': results,
            'object_list': results,
            'paginator': paginator,
            'is_paginated': paginator.count > 0,
            'page_obj': results,
        }
        return render(request, 'core/index.html', context)


search_view = SearchMillionaires.as_view()
