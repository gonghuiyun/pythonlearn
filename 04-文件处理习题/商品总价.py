'''
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

2. 修改文件内容，把文件中的mac都替换成linux
'''
sum=0
with open('a.txt','r') as ori:
    for i in range(5):
        data=ori.readline()
        data_split=data.split(' ')
        name=data_split[0]
        val=data_split[1]
        count=data_split[2]
        sum=int(val)*int(count)+sum
print(sum)
