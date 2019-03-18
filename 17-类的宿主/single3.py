'''
3.    除了文中讲到的方法之外，另外用至少4种方式实现单例模式
方法3：使用元类定义返回对象的方法
'''
import settings

instance = None

class SingleType(type):
    global instance

    def __init__(self, class_name, class_base, class_dict):
        pass

    #调用对象时执行
    def __call__(self, *args, **kwargs):
        global instance
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)
        if instance is None:
            instance = obj #第一次调用时会执行
        return instance


class MySQL(object, metaclass=SingleType):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def read_from_conf(cls):
        obj = cls(settings.IP, settings.PORT)
        return obj


obj4 = MySQL.read_from_conf()
obj5 = MySQL.read_from_conf()
obj6 = MySQL.read_from_conf()
print(obj4)
print(obj5)
print(obj6)
