from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSets, FollowViewSets

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename="posts")
router_v1.register(r'groups', GroupViewSet, basename="groups")
router_v1.register(r'follow', FollowViewSets, basename="follows")
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSets, basename="comments")

urlpatterns = [
    path(r'v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls))
]
