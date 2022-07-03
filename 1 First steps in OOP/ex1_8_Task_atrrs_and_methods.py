# 1.8 Испытание свойствами и методами


class Router:
    def __init__(self):
        self.buffer = []
        self.linked_servers = {}

    def link(self, server):
        self.linked_servers[server.get_ip()] = server
        server.linked_router = self

    def unlink(self, server):
        server_ip = server.get_ip()
        if server_ip in self.linked_servers:
            self.linked_servers.pop(server_ip)
            server.linked_router = None

    def send_data(self):
        for data_entry in self.buffer:
            if data_entry.ip in self.linked_servers:
                self.linked_servers[data_entry.ip].buffer.append(data_entry)
        self.buffer.clear()


class Server:
    __ip_next = 0

    def __new__(cls, *args, **kwargs):
        cls.__ip_next += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = self.__ip_next
        self.buffer = []
        self.linked_router = None

    def send_data(self, data):
        if self.linked_router:
            self.linked_router.buffer.append(data)

    def get_data(self):
        output_buff = self.buffer
        self.buffer = []
        return output_buff

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


sv = Server()
print(sv.ip)
print(sv.__dict__)

sv.buffer = [1, 2, 3]
print(sv.get_data())
print(sv.__dict__)

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello there!", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print('sv_to data: ', *(x.data for x in msg_lst_to))
print('sv_from data: ', *(x.data for x in msg_lst_from))

print(sv_from.__dict__, sv_from2.__dict__, sv_to.__dict__, sep='\n')
print(router.__dict__)

router.unlink(sv_to)
router.unlink(sv_from)
router.unlink(sv_from2)
print(router.__dict__)

router.unlink(Server())  # ip:7
sv3 = Server()  # ip: 8
router.link(sv3)
print(router.__dict__)


