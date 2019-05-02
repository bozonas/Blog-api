from django.urls import include, path
from rest_framework import routers
from Blog_api.blog import views
from rest_framework.authtoken import views as authviews

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'login', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),

]