msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
goods_l=[]
while True:
    for key,item in msg_dic.items():
        print('name:{name} price:{price}'.format(price=item,name=key))
    choice=input('商品>>: ').strip()
    if not choice or choice not in msg_dic:continue
    count=input('购买个数>>: ').strip()
    if not count.isdigit():continue
    goods_l.append((choice,msg_dic[choice],count))

    print(goods_l)