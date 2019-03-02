import settings
class MySQL:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def read_from_conf(cls):
        obj = cls(settings.IP, settings.PORT)
        return obj


obj1 = MySQL.read_from_conf()
obj2 = MySQL.read_from_conf()
obj3 = MySQL.read_from_conf()
# print(obj4)
# print(obj5)
# print(obj6)