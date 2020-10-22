import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import threading
import time
import os, sys
import threading

running = True
flag_game = 1
SEC = 5
stub = ""
nickname = ""

def gameoff(stub, nickname):
    global flag_game, running
    flag_game = 0
    print("Вы не успели ответить за отведенное время (%s) c." % SEC)
    response = stub.Logout(helloworld_pb2.LogoutRequest(pid=nickname))
    print(response.msg)
    os._exit(1)

def run():
    pid = os.getpid()
    global flag_game
    global running
    ip = str(input("Введите IP адрес: "))
    try:
        cnl = str(ip)+":6060"
        channel = grpc.insecure_channel(cnl)
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.IP(helloworld_pb2.IPRequest(address=ip))
        print("Сервер: " + response.message + '\n')
    except:
        print("Не удалось подключиться к серверу, перезапустите программу")
        running = False
        os._exit(1)

    login = str(input("Введите логин: "))
    response = stub.Login(helloworld_pb2.LoginRequest(name=login))
    nickname = login
    print("Сервер: \n" + response.message + '\n')


    lobby = str(input("Введите название доступного лобби или напишите 's', чтобы создать свое лобби: "))
    if lobby == 's':
        cod = '1'
        response = stub.Lobby(helloworld_pb2.LobbyRequest(code=cod, name=nickname))
    else:
        cod = '2'
        response = stub.Lobby(helloworld_pb2.LobbyRequest(code=cod, name=lobby))
    print(response.message)
    log_check = response.code
    while log_check != '1':
        #print("Такого лобби не существует")
        lobby = str(input("Введите название доступного лобби или напишите 's', чтобы создать свое лобби: "))
        if lobby == 's':
            cod = '1'
            response = stub.Lobby(helloworld_pb2.LobbyRequest(code=cod, name=nickname))
        else:
            cod = '2'
            response = stub.Lobby(helloworld_pb2.LobbyRequest(code=cod, name=lobby))
        print(response.message)
        log_check = response.code

    while flag_game == 1 and running:
        Timer = threading.Timer(SEC, gameoff, [stub, nickname])
        Timer.start()
        command = str(input("%s: " % nickname))
        if command == "" or command == "exit":
            response = stub.Logout(helloworld_pb2.LogoutRequest(pid=nickname))
            print(response.msg)
            flag_game = 0
            os._exit(1)
        response = stub.Command(helloworld_pb2.CommandRequest(msg=command, pid=nickname))

        # print(response.msg)
        if response.letter == "exit":
            print("Такого города не существует. Игра окончена")
            response = stub.Logout(helloworld_pb2.LogoutRequest(pid=nickname))
            print(response.msg)
            flag_game = 0
            os._exit(1)
        else:
            Timer.cancel()
            print("Следующий ход. Буква '%s'" % response.letter)
    #print("Сервер: " + response.message + '\n', "code ", response.code)

if __name__ == '__main__' and running:
    run()
