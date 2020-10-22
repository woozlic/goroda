import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import threading
import time
import os

flag_game = 1


def gameoff():
    global flag_game
    flag_game = 0
    # print("Вы не успели ответить за отведенное время (%s) c." % SEC)


def run():
    pid = os.getpid()
    global flag_game
    channel = grpc.insecure_channel('localhost:6060')

    stub = helloworld_pb2_grpc.GreeterStub(channel)
    login = str(input("Введите логин: "))
    response = stub.Login(helloworld_pb2.LoginRequest(name=login))
    nickname = login
    print("Сервер: \n" + response.message + '\n')


if __name__ == '__main__':
    run()
