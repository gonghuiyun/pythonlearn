'1 自定义函数模拟range(1,7,2)'
def range(s,e,step):
    while s+step<e:
        yield s
        s+=step

a=range(1,7,2)
for i in a:
    print(i)

'''
2、模拟管道，实现功能:tail -f access.log | grep '404'
'''
import time
def tail(filepath):
    with open(filepath,'rb') as f:
        f.seek(0,2)
        while True:
            line=f.readline()
            if line:
                yield line
            else:
                time.sleep(0.2)

def grep(pattern,lines):
    for line in lines:
        line=line.decode('utf-8')
        if pattern in line:
            yield line

for line in grep('404',tail('a.txt')):
    print(line,end='')

'''
3、编写装饰器，实现初始化协程函数的功能
'''
def init(func):
    def tmp(*args):
        g=func(*args)
        next(g)
        return g
    return tmp

@init
def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)

g=eater('albert')
g.send('a')
