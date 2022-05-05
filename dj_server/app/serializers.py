from django_grpc_framework import proto_serializers

import author_pb2
from app.models import Author


class AuthorProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Author
        proto_class = author_pb2.AuthorResponse
        fields = [
            'id',
            'name',
            'surname',
        ]
