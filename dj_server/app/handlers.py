import author_pb2_grpc
from .services import AuthorService


def grpc_handlers(server):
    author_pb2_grpc.add_AuthorServiceServicer_to_server(AuthorService.as_servicer(), server)
