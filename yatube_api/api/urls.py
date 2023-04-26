from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import GroupViewSet, CommentViewSet, FollowViewSet, PostViewSet

router = SimpleRouter()
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='followers')
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
