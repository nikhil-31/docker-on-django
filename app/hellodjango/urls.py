import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from upload.views import image_upload
from tasks.views import home, run_task, get_status
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("upload/", image_upload, name="upload"),
    path("tasks/<task_id>/", get_status, name="get_status"),
    path("tasks/", run_task, name="run_task"),
    path("search/", include("search.urls")),
    path("blog/", include('blog.urls')),
    path("cache/", include('cacheredis.urls')),
    path("polls/", include('polls.urls')),
    path("todos/", include('todo.urls')),
    path("__debug__/", include(debug_toolbar.urls)),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
