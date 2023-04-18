from django.urls import path, include
from rest_framework import routers

from blog.views import UserViewSet, CategoryViewSet, ArticleViewSet, \
    SearchUsers, SearchArticles, SearchCategories

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'article', ArticleViewSet)

urlpatterns = [
    path('user/<str:query>/', SearchUsers.as_view()),
    path('category/<str:query>/', SearchCategories.as_view()),
    path('article/<str:query>/', SearchArticles.as_view()),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include(router.urls)),
]
