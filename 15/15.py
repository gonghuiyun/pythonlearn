'''
实现这样一个功能，有一个对象，他有一个count属性，
count属性是统计他所在的类产生了多少个对象，
即print(obj.count)能打印出对象的个数
'''

# class any:
#     count=0
#     def __init__(self):
#         any.count=any.count+1
#
#
# obj1=any()
# obj2=any()
# obj3=any()
# obj4=any()
# print(any.count)

'''
实现一个人狗大战的程序，人可以咬狗，
狗也可以咬人，人和狗都有自己的生命值，
被咬了之后会掉血，当生命值为0时，人或者狗就死了
'''
# import random
# print(random.randint(50,100))
import time
class person:
    def __init__(self, name, bat, life):
        self.name = name
        self.bat = bat
        self.life = life

    def bite(self,bite):
        self.life -= bite

class dog:
    def __init__(self, name, bat, life):
        self.name = name
        self.bat = bat
        self.life = life

    def bite(self, bite):
        self.life -= bite

person1 = person('张二炮', 60, 100)
person2 = person('刘老三', 50, 100)

dog1 = dog('旺财', 80, 50)
dog2 = dog('小黑', 200, 200)

list_person = [person1, person2]
list_dog = [dog1, dog2]

while len(list_person) & len(list_dog) > 0:
    if len(list_person) > 0:
       for i in list_person:
           print('human: ', i.name)
           if len(list_dog) > 0:
               for j in list_dog:
                   print('dog:', j.name)
                   i.bite(j.bat)
                   print('hume_life: ', i.life)
                   if i.life > 0:
                       j.bite(i.bat)
                       print('dog_life: ', i.life)
                   else:
                        list_person.remove(i)
                        break
                   if j.life < 0:
                       list_dog.remove(j)
           else:
               print('dog fail')
               time.sleep(2)
               break
    else:
        print('human fail')
        time.sleep(2)
        break

# print(person1.life)
# print(person2.life)
# print(dog1.life)
# print(dog2.life)

