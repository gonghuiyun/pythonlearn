dic={
    'a':{'math':'90','music':'91'},
    'b':{'math':'92','music':'93'},
    'c':{'math':'94','music':'95'}
}

OneCList={
        'a':' ',
        'b':' ',
        'c': ' '
        }

class Score:
    def __init__(self,name,course):
        self.NAME = name
        self.COURSE = course

    def getList(self):
        return dic[self.NAME]

    def getCScore(self):
        return dic[self.NAME][self.COURSE]

    def ave(self):
        sum=0
        count=0
        for i,j in dic[self.NAME].items():
            sum += int(j)
            count = count+1
        return sum/count

    def OneCAll(self):
        for i, j in dic.items():
            OneCList[i] = j[self.COURSE]
        return  OneCList

name = input('please input your name: ')
course=input('please input the course: ')

pro = Score(name,course)
print('score list: ', pro.getList())
print('score of one course ', pro.getCScore())
print('ave score: ', pro.ave())
print('math of all: ',pro.OneCAll())

