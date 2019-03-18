'''
3.    除了文中讲到的方法之外，另外用至少4种方式实现单例模式
方法2：使用装饰器
'''
import settings
instance = None

class MySQL:
    global instance

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def single(func):
        global  instance
        def tmp(*args,**kwargs):
            global instance
            res = func(*args,**kwargs)

            if instance is None:
                instance = res #第一次调用时会执行
            return instance
        return tmp

    @single
    # @classmethod
    def read_from_conf(cls):
        obj = cls(settings.IP, settings.PORT)
        return obj



obj4 = MySQL.read_from_conf(MySQL)
obj5 = MySQL.read_from_conf(MySQL)
obj6 = MySQL.read_from_conf(MySQL)
print(obj4)
print(obj5)
print(obj6)
