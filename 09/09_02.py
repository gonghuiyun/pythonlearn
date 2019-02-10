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