"""
有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，
将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
"""
l=[11,22,33,44,55,66,77,88,99,90]
l1=[]
l2=[]
dict={'k1':l1,'k2':l2}
for i,j in enumerate(l,0):
    print(j)
    if j>66:
        l1.append(j)
    else:
        l2.append(j)
print(dict)
