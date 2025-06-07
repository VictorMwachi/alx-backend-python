from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('messages',MessageViewSet)
router.register('conversation',ConversationViewSet)
router.register('user',UserViewSet)
urlpatterns = router.urls
#urlpatterns = [
#    path('/',MessageViewSet.queryset),
#]