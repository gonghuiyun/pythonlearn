'''
1. 有列表l=['a','b',1,'a','a']，列表元素均为可不可变类型，
去重，得到新列表,且新列表无需保持列表原来的顺序
2.在上题的基础上，保存列表原来的顺序
'''
l=['a','b',1,'a','a']
l1=[]
s=set()
for i in l:
    if i not in s:
        s.add(i)
        l1.append(i)
print(s)
print(l1)