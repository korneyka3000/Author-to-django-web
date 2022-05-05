from django_grpc_framework.services import Service
from .models import Author
from .serializers import AuthorProtoSerializer


class AuthorService(Service):
    def GetAuthors(self, request, context):
        authors = Author.objects.all()
        serializer = AuthorProtoSerializer(authors, many=True)
        for author in serializer.message:
            yield author
