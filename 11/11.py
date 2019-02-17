'''
1、将names=['albert','james','kobe','kd']中的名字全部变大写
'''

names=['albert','james','kobe','kd']
change=[print(i.upper())for i in names]

'''
2、将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，
然后保存剩下的名字长度
'''
names=['albert','jr_shenjing','kobe','kd']

tmp=('%s' % i for i in names)
name_new=[]
for i in range(len(names)):
    name_spli=next(tmp).split('_')
    print(len(name_spli[0]))

# names=[len(name) for name in names if not name.endswith('shenjing')]
# print(names)

'''
3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
'''

with open('a.txt','r') as f:
    list=[len(line) for line in f]
print(max(list))

'''
4、求文件a.txt中总共包含的字符个数？
思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
'''
sum1=0
with open('a.txt','r') as f:
    sum1=sum(len(line) for line in f)
print(sum1)

#思考题，光标到了文件结尾，经过修改光标位置输出正常
with open('a.txt', encoding='utf-8') as f:
    print(sum(len(line) for line in f))
    f.seek(0, 0)
    print(sum(len(line) for line in f))
    f.seek(0, 0)
    print(sum(len(line) for line in f))

'''
5、思考题
with open('a.txt') as f:
    g=(len(line) for line in f)
print(sum(g)) #为何报错？
'''
with open('a.txt') as f:
    g=(len(line) for line in f)
print(sum(g)) #为何报错？
#错误的原因：ValueError: I/O operation on closed file.

'''
lenovo,3000,10
tesla,1000000,10
chicken,200,1
（1）求总共花了多少钱？

（2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]

（3）求单价大于10000的商品信息,格式同上
'''

#（1）求总共花了多少钱？
import numpy as np
with open('shopping.txt','r') as f:
    l1 = [int(line.split(',')[1]) for line in f]
    f.seek(0 , 0)
    l2 = [int(line.split(',')[2]) for line in f]
    print(np.dot(l1,l2))

#打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
dic={}
dic=dict.fromkeys(['name','price','count'])
print(dic)
with open('shopping.txt','r') as f:
    for line in f:
        line_split=line.split(',')
        dic['name']=line_split[0]
        dic['price'] = line_split[1]
        dic['count'] = int(line_split[2])
        print(dic)

#（3）求单价大于10000的商品信息,格式同上
dic={}
dic=dict.fromkeys(['name','price','count'])
with open('shopping.txt','r') as f:
    for line in f:
        line_split=line.split(',')
        dic['name']=line_split[0]
        dic['price'] = line_split[1]
        dic['count'] = int(line_split[2])
        if int(dic['price'])>10000:
            print(dic)

