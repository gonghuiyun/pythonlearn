'''
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

2. 修改文件内容，把文件中的mac都替换成linux
'''
import os
with open('a.txt','r') as ori,open('b.txt','w') as tmp:
    for line in ori:
        data=line.replace('mac','linux')
        tmp.write(data)
os.remove('a.txt')
os.rename('b.txt','a.txt')
