# Title: CMPE273-Lab2
# Description: A simple calculator with add(x, y) function as a gRPC server
# By: Neil Shah

from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculateStub(channel)

        response = stub.Add(calculator_pb2.AddRequest(a=2, b=3))
        print("Calculator clinet received: " + response.message)


if __name__ == '__main__':
    run()
