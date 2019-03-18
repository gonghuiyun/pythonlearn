1.    类的属性和对象的属性有什么区别?
类的属性是指定义在类内的属性，对象的属性是定义在__init__内的
2.    什么是绑定到对象的方法，如何定义，如何调用，给谁用？有什么特性
类内定义的函数，给对象用的，为绑定到对象的放那该法。
定义时将对象作为第一个参数传入。
调用：obj.func()，给对象用。
特性是只对本对象有效
3.    什么是多态，多态有哪些优点，可以在哪些场景使用多态
多态：在父类中的某种方法，子类的对象可以直接调用
多态的有点：可以在不用考虑的对象具体类型的前提下，直接使用对象下的方法
场景：如定义动物的某个属性，不同类型的动物实现方式不同

4.    以自己的理解简述一下Python中鸭子类型，可以查阅资料，举出一个简单实例(代码实现)
只要看起来类似的类型，都使用同一个名称的方法，
这样不用关心对象到底是什么类型，只要关心对象的行为
```
class duck:
  def bark(self):
    print('ga!')

class bird:
  def bark(self):
    print('ga!')

def bark_all(x):
  x.bark()

obj_duck = duck()
obj_bird = bird()
bark_all(obj_duck)
bark_all(obj_bird)

输出：
ga!
ga!
```
5.什么是封装，封装有哪些优点
装就是把一对属性存起来，封就是把这些属性隐藏起来。
优点：需要专门开辟接口给类外部的使用者使用，
我们可以在接口之上添加任意控制逻辑，从而严格控制访问者对属性的操作，隔离复杂度。

6.教程中封装那一节的小问题
```
class Foo:
    __x = 111 

    def __init__(self,y):
        self.__y = y
    def __f1(self):
        print('Foo.f1')
    def get__y(self):  # 这个get__y属性肯定是能访问到的啊
        print(self.__y)

obj = Foo(222)

obj.get__y()
输出：222
```
解释：因为get__y是对象的方法，对象可以访问它。而它是属于类内的方法，可以访问类内隐藏的变量。

11.不运行程序看代码说出代码运行结果并解释
```
class Parent(object):   
	x = 1 
class Child1(Parent):   
	pass 
class Child2(Parent):   
	pass 

print(Parent.x, Child1.x, Child2.x) 
#1 1 1 ，子类继承了父类
Child1.x = 2
print(Parent.x, Child1.x, Child2.x) 
#1 2 1 ，child2继承了父类，
child1 被添加了属性x，因此优先用自己的属性
Parent.x = 3
print(Parent.x, Child1.x, Child2.x) 
#3 2 3， child2继承了父类，因父类改变，所以它也改变。
child1 之前被添加了属性x，因此优先用自己的属性
```