# Title: CMPE273-Lab2
# Description: A simple calculator with add(x, y) function as a gRPC server
# By: Neil Shah

from concurrent import futures
import time

import grpc

import calculator_pb2
import calculator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculate(calculator_pb2_grpc.CalculateServicer):

    def Add(self, request, context):
        return calculator_pb2.AddReply(message="Sum of %s and %s is %s" % (str(request.a), str(request.b), str(request.a+request.b)))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculateServicer_to_server(Calculate(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
