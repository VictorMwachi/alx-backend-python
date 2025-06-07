from django.urls import path
import rest_framework.routers as router
from .views import *

router = routers.DefaultRouter()
router.register('messages',MessageViewSet)
router.register('conversation',ConversationViewSet)
router.register('user',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]