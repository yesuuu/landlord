import asyncore, socket
from asyncore import dispatcher
from asynchat import async_chat


class ChatSession(async_chat):

    def __init__(self, sock):
        async_chat.__init__(self, sock)
        self.set_terminator('\r\n')
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = 'b'.join(self.data)
        self.data = []
        print line


class ChatServer(dispatcher):

    def __init__(self, port, listenNum=5):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(listenNum)

        self.sessions = []

    def handle_accept(self):
        conn, addr = self.accept()
        print 'connect from', addr[0]
        self.sessions.append(ChatSession(conn))

    def broadcast(self):
        pass


if __name__ == '__main__':
    s = ChatServer(5005)
    asyncore.loop()

