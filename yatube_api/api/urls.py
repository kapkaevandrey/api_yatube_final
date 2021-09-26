from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSets, FollowViewSets

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSets)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSets, basename="comments")

urlpatterns = [
    path(r'v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls))
]
