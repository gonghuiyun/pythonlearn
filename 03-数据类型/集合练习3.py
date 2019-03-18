'''
4.有如下列表，列表元素为可变类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
l=[
    {'name':'albert','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'albert','age':20,'sex':'female'},
    {'name':'albert','age':18,'sex':'male'},
    {'name':'albert','age':18,'sex':'male'},
]
'''

l=[
    {'name':'albert','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'albert','age':20,'sex':'female'},
    {'name':'albert','age':18,'sex':'male'},
    {'name':'albert','age':18,'sex':'male'},
]
l1=[]
s=set()
for i in l:
    val=(i['name'],i['age'],i['sex'])
    if val not in s:
        s.add(val)
        l1.append(i)
print(l1)

