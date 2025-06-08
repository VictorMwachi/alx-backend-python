from django.urls import path, include
import rest_framework.routers as routers, NestedDefaultRouter
from .views import *

router = routers.DefaultRouter()
router.register('messages',MessageViewSet)
router.register('conversation',ConversationViewSet)
#router.register('user',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]