from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    										TokenObtainPairView,
    										TokenRefreshView,)

from .views import (PostViewSet, CommentViewSet, 
					GroupViewSet, FollowViewSet)


router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet, basename='posts')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='post_id')
router_v1.register('v1/group', GroupViewSet, basename='groups')
router_v1.register('v1/follow', FollowViewSet, basename='followers')


urlpatterns = router_v1.urls


urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', obtain_auth_token),
]
