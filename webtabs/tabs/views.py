from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.generics import RetrieveDestroyAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .repositories import *
from .services import get_ogp


# Create your views here.


class CollectionViewSet(ModelViewSet):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionSerializer

    def get_queryset(self):
        return CollectionRepository.get_queryset(self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class WebTagRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    serializer_class = WebTagSerializer

    def get_queryset(self):
        return WebTagRepository.get_queryset(self.request.user)


class WebTagListAPIView(ListAPIView):
    """Список всех закладок"""
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    serializer_class = WebTagSerializer

    def get_queryset(self):
        return WebTagRepository.get_queryset(self.request.user)


class WebTagCreateAPIView(APIView):
    """
    Создание закладки
    """
    serializer_class = WebTagSerializer

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'url': openapi.Schema(type=openapi.TYPE_STRING, description='url веб страницы для создания закладки'),
        },
        required=['url']
    ),
        responses={
            status.HTTP_201_CREATED: WebTagSerializer()
        }
    )
    def post(self, request):
        data = get_ogp(request.data['url'], request.user)
        if data:
            return Response(self.serializer_class(data).data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'url does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)


class AddWebTagToCollection(APIView):
    """
    Добавление закладки в коллекцию по id
    """
    serializer_class = WebTagSerializer

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'web_tag_id': openapi.Schema(type=openapi.TYPE_STRING,
                                         description='id закладки, которую требуется добавить в коллекцию'),
            'collection_id': openapi.Schema(type=openapi.TYPE_STRING,
                                            description='id коллекции, в которую нужно добавить закладку'),
        },
        required=['web_tag_id', 'collection_id']
    ),
        responses={
            status.HTTP_202_ACCEPTED: WebTagSerializer()
        }
    )
    def post(self, request):
        data = WebTagRepository.add_collection(request.data['web_tag_id'], request.data['collection_id'])
        if data:
            return Response(self.serializer_class(data).data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                'error': 'Object does not exists'
            }, status=status.HTTP_400_BAD_REQUEST)
