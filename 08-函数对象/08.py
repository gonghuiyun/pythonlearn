'''
1 写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
'''
def refine(x,y):
    with open(x,'a') as f:
        f.write(str(y))
refine('a.txt',3)
'''
2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
'''
def count(x):
    digit=0
    alp=0
    spa=0
    another=0
    for i in x:
        if i.isdigit():
            digit=digit+1
        elif i.isalpha():
            alp=alp+1
        elif i.isspace():
            spa=spa+1
        else:
            another=another+1
    print('{digit},{alpha},{space},{other}'.format(digit=digit,alpha=alp,space=spa,other=another))
count('a1 33 adf are*')

'''
3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
'''
def heigher(x):
    if len(x)>5:
        print('length is > 5')
heigher([1,2,3,4,5,6])

'''
4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
'''
def two(x):
    if len(x)<3:
        print(x)
    else:
        print(x[0:2])
two([1,2,3])
two([1,2])

'''
5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
'''
def odd(x):
    l=[]
    for i in enumerate(x):
        if i[0] % 2 != 0:
            l.append(i[1])
    return l

l1=['a','b','c','d']
l2=odd(l1)
print(l2)

'''
6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
'''

def dic_refine(dic):
    for i in dic.items():
        if len(i[1]) > 3:
            dic[i[0]] = i[1][0:2]
    return dic
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
print(dic_refine(dic))


