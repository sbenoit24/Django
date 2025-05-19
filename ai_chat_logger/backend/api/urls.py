from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, CustomAuthToken, ChatSessionViewSet, ChatMessageViewSet

router = DefaultRouter()
router.register('sessions', ChatSessionViewSet, basename='session')
router.register('messages', ChatMessageViewSet, basename='message')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('', include(router.urls)),
]
