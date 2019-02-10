'''
5 编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
'''
import time

tag=False

def login():
    global tag
    name=input('please input your name: ')
    if tag==False:
        with open('a.txt','r') as f:
            for line in f:
                dic=eval(line)
                if dic['name']==name:
                    password = input('please input your password: ')
                    if dic['password']==password:
                        tag=True

def time_count(func):
    global tag
    start=time.time()
    func()
    end = time.time()
    #if end-start>3.4836273193359375e-05:
    if end - start > 3:
        print('time out and please login again')
        tag=False

def final(func):
    def processing():
        while True:
            if tag==False:
                login()
            else:
                time_count(func)
                if tag==False:
                    continue
                else:
                    break
    return processing

@final
def pri():
   print('aaaaaa')

@final
def pri2():
    time.sleep(4)
    print('bbbbb')

pri()
pri2()

'''
6 编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
'''
from urllib.request import urlopen

def index(url):
    def get():
        return urlopen(url).read()
    return get

baidu=index('http://www.baidu.com')
print(baidu().decode('utf-8'))

'''
7 为题目五编写装饰器，实现缓存网页内容的功能：
具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，
否则，就去下载，然后存到文件中新登录
'''
import time
from urllib.request import urlopen

tag=False
name_url='http://www.baidu.com'

def login():
    global tag
    name=input('please input your name: ')
    if tag==False:
        with open('a.txt','r') as f:
            for line in f:
                dic=eval(line)
                if dic['name']==name:
                    password = input('please input your password: ')
                    if dic['password']==password:
                        tag=True

def time_count(func):
    def tmp1(*args):
        global tag
        start=time.time()
        func(name_url)
        end = time.time()
        print(end-start)
        #if end-start>3.4836273193359375:
        if end - start > 0.04628973007202148:
            tag = False
            print('time out and please login again')
    return tmp1

def login_final(func):
    global tag
    def tmp3(*args):
        global tag
        if tag==False:
            login()
            func(*args)
            if tag==False:
                login()
    return tmp3

@login_final
@time_count
def index(url):
    tmp=urlopen(url).read()
    data=tmp.decode('utf-8')
    with open('b.html','w') as f:
        f.write(data)

index(name_url)

'''
8 在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作。。有疑问！！！！！！)
'''
route_dic={}
def save(name):
    def tmp(func):
        route_dic[name]=func
    return tmp

@save('select')
def f1():
    print('aaa')

@save('delete')
def f2():
    print('bbb')

print(route_dic)

'''
9 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
注意：时间格式的获取
'''
import time

name='c.txt'

def log(filename):
    def tmp(func):
        func()
        with open(filename,'a') as f:
            f.write(time.strftime('%Y-%m-%d %X'))
            f.write('\n')
    return tmp

@log(name)
def f1():
    print('aaaaaa')

f1




