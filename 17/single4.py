'''
3.    除了文中讲到的方法之外，另外用至少4种方式实现单例模式
方法4：使用__new__方法
'''
import settings

class MySQL:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def read_from_conf(cls):
        obj = cls(settings.IP, settings.PORT)
        return obj

    #创建对象时执行
    def __new__(cls, *args, **kwargs):
        if not hasattr(MySQL, "_instance"):
                MySQL._instance = object.__new__(cls) #第一次调用时会执行
        return MySQL._instance


obj4 = MySQL.read_from_conf()
obj5 = MySQL.read_from_conf()
obj6 = MySQL.read_from_conf()
print(obj4)
print(obj5)
print(obj6)
