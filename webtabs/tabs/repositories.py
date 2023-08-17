from .models import *


class CollectionRepository:

    @staticmethod
    def get_queryset(author):
        return Collection.objects.filter(author=author)

    @staticmethod
    def get(pk: int):
        return Collection.objects.get(pk=pk)


class WebTagRepository:

    @staticmethod
    def get_queryset(author):
        return WebTag.objects.filter(author=author)

    @staticmethod
    def add(data):
        return WebTag.objects.create(**data)

    @staticmethod
    def add_collection(web_tag_id, collection_id):
        try:
            tag = WebTag.objects.get(pk=web_tag_id)
            tag.collection = CollectionRepository.get(collection_id)
            tag.save(update_fields=['collection'])
            return tag
        except models.ObjectDoesNotExist:
            return
