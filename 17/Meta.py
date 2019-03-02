'''
2.    自定义轿车元类CarMeta，实现元类为CarMeta的类至少有生产日期(production_date)、
发动机编号(engine_number)及载客量(capacity)三个基本属性，没有就不行
'''


class CarMeta(type):
    # 创建类
    def __init__(self, class_name, class_bases, class_dic):
        pass
        super(CarMeta, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)

        if not hasattr(obj,"production_date"):
            raise TypeError('production_date')
        if not hasattr(obj,"engine_number"):
            raise TypeError('engine_number')
        if not hasattr(obj,"capacity"):
            raise TypeError('capacity')
        return obj


class Car1(object, metaclass=CarMeta):

    def __init__(self,production_date,engine_number,capacity):
        # self.production_date = production_date
        self.engine_number = engine_number
        self.capacity = capacity

obj = Car1(1,2,3)
