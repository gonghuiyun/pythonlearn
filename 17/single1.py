'''
3.    除了文中讲到的方法之外，另外用至少4种方式实现单例模式
方法1：使用模块导入
'''

from sql import obj1 as obj1
from sql import obj1 as obj2
from sql import obj1 as obj3
from sql import obj1 as obj4

#对象 obj1在 sql.py里创建，只有第一行‘from sql import obj1 as obj1’
# 在导入时才执行模块，因此始终只有一个obj1对象
print(obj1)
print(obj2)
print(obj3)
print(obj4)