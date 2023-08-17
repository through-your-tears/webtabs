from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CollectionViewSet, WebTagCreateAPIView, WebTagRetrieveDestroyAPIView, AddWebTagToCollection, \
    WebTagListAPIView


router = DefaultRouter()
router.register(r'collections', CollectionViewSet, 'collection')
urlpatterns = [
    path('webtag/<int:pk>/', WebTagRetrieveDestroyAPIView.as_view()),
    path('webtag/add_collection/', AddWebTagToCollection.as_view()),
    path('webtag/list/', WebTagListAPIView.as_view()),
    path('webtag/', WebTagCreateAPIView.as_view()),
]
urlpatterns += router.urls
