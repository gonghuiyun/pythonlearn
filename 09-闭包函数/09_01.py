'''
装饰器例子：
import time

def outer(func):
    def timer():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return timer

@outer
def index():
    time.sleep(1)
    print('index')

def home(name):
    time.sleep(1)
    print('home')

index()

'''
'''
1 编写函数，（函数执行的时间是随机的）
'''
import random
import time

time_ram = random.random()

def random(func):
    print('sleep: ',time_ram)
    time.sleep(time_ram)
    return func

@random
def pri():
    print('a')

pri()

'''
编写装饰器，为函数加上统计时间的功能
'''
import time

def consol(func):
    def count_time():
        start=time.time()
        func()
        end=time.time()
        print('time is: ',end-start)
    return  count_time

@consol
def pri():
    print('a')

pri()

'''
3 编写装饰器，为函数加上认证的功能
'''
def pri_login(func):
    def login():
        flag=False
        name = input('please input your name: ')
        with open('a.txt','r') as f:
            for line in f:
                dic=eval(line)
                if dic['name']==name:
                     password = input('please input your password: ')
                     if dic['password']==password:
                        func()
                        flag=True
        if flag==False:
            print('this user dont exit!')
    return login

@pri_login
def pri():
    print('a')

pri()

'''
4 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）
    要求：
        登录成功一次，后续的函数都无需再输入用户名和密码
    注意：
        从文件中读出字符串形式的字典，可以用
        eval('{"name":"albert","password":"123"}')转成字典格式
'''
tag=False
def pri_login(func):
    def login():
        global tag
        if tag==False:
            name = input('please input your name: ')
            with open('a.txt','r') as f:
                for line in f:
                    dic=eval(line)
                    if dic['name']==name:
                         password = input('please input your password: ')
                         if dic['password']==password:
                            func()
                            tag=True
        else:
            func()
    return login

@pri_login
def pri():
    print('a')

@pri_login
def pri2():
    print('b')

pri()
pri2()






