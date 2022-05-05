import grpc
from django.shortcuts import render
from google.protobuf.json_format import MessageToDict

import author_pb2_grpc
import author_pb2
from app.models import Author


def main_view(request):
    if request.method == 'POST':
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = author_pb2_grpc.AuthorServiceStub(channel)
            arr = []
            for author in stub.GetAuthors(author_pb2.AuthorResponse()):
                d = MessageToDict(author)
                if not Author.objects.filter(name=d['name'], surname=d['surname']).exists():
                    Author.objects.create(name=d['name'], surname=d['surname'])
                    arr.append(d)
            context = {
                'arr': arr,
            }
            return render(request, 'home.html', context)
    context = {}
    return render(request, 'home.html', context)
