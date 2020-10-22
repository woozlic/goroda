from concurrent import futures
import grpc
import helloworld_pb2_grpc, helloworld_pb2
import time
import socket
print(socket.gethostbyname(socket.gethostname()))

TIMER = 5
#python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/helloworld.proto

path = "cities/"
players = []
lobbies = []

def addlobbie(p):
    global lobbies
    lobbies.append([p])
def addplayer(p, host):
    global lobbies
    for i in lobbies:
        if i[0].nick == host:
            i.append(p)
            return 1
def printlobbies():
    global lobbies
    for i in range(len(lobbies)):
        try:
            print("Лобби №{%s}:" % str(i+1))
            for j in lobbies[i]:
                print(j.nick,)
        except:
            print("Нету лобби")
def delplayerfromlobby(nick):
    global lobbies
    for i in range(len(lobbies)):
        if len(lobbies[i])==1:
            del lobbies[i]
        else:
            for j in range(len(lobbies[i])):
                if str(lobbies[i][j].nick)==str(nick):
                    del lobbies[i][j]
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
    global players
    global lobbies
    def Login(self, request, context):
        self.p = Player(request.name)
        players.append(self.p)
        return helloworld_pb2.LoginReply(message='Привет, %s!' % (request.name))
    def Logout(self, request, context):
        for p in range(len(players)):
            if str(request.pid) == str(players[p].nick):
                del players[p]
                break
        delplayerfromlobby(str(request.pid))
        return helloworld_pb2.LogoutReply(msg = "Вы были исключены из игры")
    def AddLobbie(self, nick):
        lobbies.append([nick])
    def AddPlayerToLobby(self, nick, lobby):
        for i in lobbies:
            if i[0].nick == lobby:
                i.append(nick)
                return 1
    def LogoutLobby(self, nick):
        for i in range(len(lobbies)):
            if len(lobbies[i]) == 1:
                del lobbies[i]
            else:
                for j in range(len(lobbies[i])):
                    if str(lobbies[i][j].nick) == str(nick):
                        del lobbies[i][j]
    def Lobby(self, request, context):
        code = request.code
        lobby = request.name
        message = ''
        res = 0
        if code == "1":
            try:
                addlobbie(self.p)
                res = 1
                message = "Вы успешно создали лобби. Введите название любого города"
            except:
                message = "Не удалось создать лобби"
                res = 0
        else:
            res = addplayer(self.p, lobby)
            if res == 1:
                message = "Вы успешно подключились к лобби. Введите название любого города"
            else:
                message = "Не удалось подключиться к лобби"
                res = 0
        return helloworld_pb2.LobbyReply(message='%s' % message, code=str(res))
    def IP(self, request, context):
        global lobbies
        listlobbies = ""
        for i in lobbies:
            listlobbies += str(i[0].nick) + " "
        return helloworld_pb2.IPReply(message='Вы подключились к серверу %s\nДоступные лобби: %s' % (request.address, listlobbies))

    def Command(self, request, context):
        # if request.msg == "s":
        #   self.game()
        # print(context)
        word = request.msg
        if exist(word):
            next_letter = word[-1]
            if next_letter in ('ь', 'ъ'):
                next_letter = word[-2]
            # message = "Следующий ход. Буква '%s'" % next_letter
        else:
            # message = "Такого города не существует. Вы выбываете из игры."
            next_letter = 'exit'
            self.Logout(request, context)
            self.LogoutLobby(request.pid)
            # print("request.pid: ", request.pid)
        return helloworld_pb2.CommandReply(letter=next_letter)
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
            print("\n")
            printlobbies()
            time.sleep(TIMER)
    except KeyboardInterrupt:
        server.stop(0)
if __name__ == '__main__':
    serve()