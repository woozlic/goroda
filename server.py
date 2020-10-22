from concurrent import futures
import grpc
import helloworld_pb2_grpc, helloworld_pb2
import time

TIMER = 5
#python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/helloworld.proto

path = "cities/"
players = []

def exist(word):
    if len(word)==0:
        return 0
    word = word.lower()
    first_letter = word[0]
    #print(first_letter)
    try:
        with open(path + first_letter+".txt", "r") as f:
            txt = f.read()
            lst = txt.split("\n")
            lst = [i.lower() for i in lst]
            if word in lst:
                return 1
            else:
                return 0
    except:
        return 0

class Player():
    def __init__(self, name):
        self.nick = name
    def printnick(self):
        return self.nick

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def Login(self, request, context):
        self.p = Player(request.name)
        players.append(self.p)
        return helloworld_pb2.LoginReply(message='Привет, %s!' % (request.name))
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:6060')
    server.start()
    try:
         while True:
            #print("server on: %i" % threading.active_count())
            #print(lobbies)
            print("Игроки на сервере: ",)
            try:
                for i in players:
                    print(i.nick,)
            except:
                print("Пусто")
            time.sleep(TIMER)
    except KeyboardInterrupt:
        server.stop(0)
if __name__ == '__main__':
    serve()