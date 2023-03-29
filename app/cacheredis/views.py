import datetime

import requests

from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, UpdateView, View
from .models import Product

BASE_URL = 'https://httpbin.org'


# Create your views here.
@method_decorator(cache_page(60 * 5), name='dispatch')
class APICalls(TemplateView):
    template_name = "api_calls.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{BASE_URL}/delay/2')
        response.raise_for_status()
        context['content'] = 'Results received!'
        context['current_time'] = datetime.datetime.now()
        return context


class HomePageView(View):
    template_name = 'home.html'

    def get(self, request):
        product_objects = cache.get('product_objects')

        if product_objects is None:  # NEW
            product_objects = Product.objects.all()
            cache.set('product_objects', product_objects)

        context = {
            'products': product_objects
        }

        return render(request, self.template_name, context)


class ProductCreateView(CreateView):
    model = Product
    fields = ['title', 'price']
    template_name = 'product_create.html'
    success_url = reverse_lazy('home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'price']
    template_name = 'product_update.html'

    # we overrode the post method for testing purposes
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        Product.objects.filter(id=self.object.id).update(
            title=request.POST.get('title'),
            price=request.POST.get('price')
        )
        return HttpResponseRedirect(reverse_lazy('home'))


def invalidate_cache(request):
    cache.delete('product_objects')
    url = reverse_lazy('home')
    return HttpResponseRedirect(redirect_to=url)
