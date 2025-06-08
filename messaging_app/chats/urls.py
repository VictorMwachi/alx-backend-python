from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *

router = routers.DefaultRouter()
router.register('messages',MessageViewSet)
router.register('conversation',ConversationViewSet)
#router.register('user',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]