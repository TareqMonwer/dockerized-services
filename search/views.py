from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import View
from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
from core.models import Millionaire


class SearchMillionaires(View):
    paginate_by = 16

    def get(self, request):
        search_string = request.GET.get('q')
        search_string = search_string if search_string else None
        results = []
        rank = None

        if search_string:
            vector = SearchVector('name', 'profession')
            search_query = SearchQuery(search_string)
            rank = SearchRank(vector, search_query)
            results = Millionaire.objects.prefetch_related('country', 'company', 'votes') \
                .annotate(search=vector, rank=rank).filter(search=search_query) \
                .order_by('-rank')
        
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
