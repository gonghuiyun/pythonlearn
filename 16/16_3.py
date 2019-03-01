'''
13. 使用多肽与封装设计一个虚拟宠物的程序，三个基础的宠物类
-- Cat类，Dog类，Pig类
属性：name(名字)、type(品种)，
name、type均为私有属性(对内可见，对外不可见)
type属性为成员属性(由构造器__init__方法赋初值)，
但type对外又是可读可写(利用property装饰器实现)，

name属性初始化操作由父类完成(子类利用super()来实现)

方法：eat(self)
均拥有eat的方法(父级继承)
但实现体分别可以体现出 "吃猫粮"、"吃狗粮"、"吃猪粮"不同点
(不同的实现)
一个宠物的父类 -- Pet类
属性：name(名字)
name为私有属性(对内可见，对外不可见)
name属性为成员属性(由构造器__init__方法赋初值)
但name对外又是可读可写(利用property装饰器实现)
方法：eat(self)
拥有eat的方法(没有方法的实现体，利用abc模块实现)一个主人类
-- Master类
属性：name(名字)、pet(宠物)
name、pet均为私有成员属性(具体操作同上面属性的操作)
方法：feed(self)
拥有feed方法(方法只有self一个参数，没有多余的参数)
feed方法实现要求
-- "某某"主人准备好宠物粮食
-- "某某品种"的"某某宠物"来进食
-- 吃...(调用宠物自身的eat方法)
注：""括起来的某某都是要被替换为具体的数据的创建三个宠物主人，
分别养的是不同的三种宠物三个主人进行喂食的时候，
对应养的宠物就会完成进食其他细节自由补充

'''


class Pet:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def eat(self):
        pass


class Cat(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.__type = type

    @property
    def getType(self):
        return self.__type

    def eat(self):
        return '吃猫粮'


class Dog(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.__type = type

    @property
    def getType(self):
        return self.__type

    def eat(self):
        return '吃狗粮'


class Pig(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.__type = type

    @property
    def getType(self):
        return self.__type

    def eat(self):
        return '吃猪粮'


class Master:
    def __init__(self, name, pet):
        self.__name = name
        self.__pet = pet

    def feed(self):
        print(' %s 主人准备好宠物粮食 ' % self.__name)
        print('{} {} 来进食'.format(self.__pet.getType, self.__pet.getName()))
        print(self.__pet.eat())
        print('------------')


obj_cat = Cat('喵喵 ', '蓝猫')
obj_dog = Dog('旺财', '京巴')
obj_pig = Pig('佩奇', '小香猪')

obj_person1 = Master('Kelly', obj_cat)
obj_person2 = Master('Tom', obj_dog)
obj_person3 = Master('Amy', obj_pig)

obj_person1.feed()
obj_person2.feed()
obj_person3.feed()
