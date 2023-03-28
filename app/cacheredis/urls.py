from django.urls import path

from .views import APICalls

urlpatterns = [
    path("", APICalls.as_view(), name="api_results"),
]
