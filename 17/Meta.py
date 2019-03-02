'''
2.    自定义轿车元类CarMeta，实现元类为CarMeta的类至少有生产日期(production_date)、
发动机编号(engine_number)及载客量(capacity)三个基本属性，没有就不行
'''

class CarMeta(type):
    #创建类
    def __init__(self, class_name, class_bases, class_dic):
        # super(CarMeta,self).__init__(class_name, class_bases, class_dic)
        pass
    def __call__(self, *args, **kwargs):
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj

class Car1(object,metaclass= CarMeta):
    def __init__(self, production_date, engine_number, capacity):
        self.production_date = production_date
        self.engine = engine_number
        self.capacity = capacity


#调用类，在__call__中传入Car1,并且传入参数。
# 然后创建空对象，调用对象的__init__方法
# 并用参数对这个对象初始化
obj = Car1()
