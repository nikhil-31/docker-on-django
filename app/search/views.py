from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.decorators.cache import cache_page

from .models import Quote


# Create your views here.
@method_decorator(cache_page(60 * 5), name="dispatch")
class QuoteList(ListView):
    model = Quote
    context_object_name = "quotes"
    template_name = "quote.html"


class SearchResultsList(ListView):
    model = Quote
    context_object_name = "quotes"
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Quote.objects.filter(
            Q(name__icontains=query) | Q(quote__icontains=query)
        )
