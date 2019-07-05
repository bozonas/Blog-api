from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'post', views.PostDetail)
router.register(r'posts', views.PostViewSet, basename='post')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    # path('<int:pk>/', views.PostDetail.as_view()),
]
