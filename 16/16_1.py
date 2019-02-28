'''
10. 如下示例, 在没有学习类这个概念时，数据与功能是分离的,
请用面向对象的形式优化以下代码
def exc1(host,port,db,charset):
    conn=connect(host,port,db,charset)
    conn.execute(sql)
    return xxx
def exc2(host,port,db,charset,proc_name):
    conn=connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx #
每次调用都需要重复传入一堆参数
exc1('127.0.0.1',3306,'db1',
'utf8','select * from tb1;')
exc2(‘127.0.0.1’,3306,'db1','utf8','存储过程的名字')
'''
import settings

class common:
    def __init__(self,host,port,db,charset):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset

    # def ini_config(self):
    #     return excute(settings.host,settings.port,settings.db,settings.charset)

class excute(common):
    def __init__(self,host,port,db,charset,p1,p2):
        super().__init__(host,port,db,charset)
        self.p1= 'select * from tb1'
        self.p2 = '存储过程的名字'

    def exc1(self):
        # conn = connect(host, port, db, charset)
        # conn.execute(sql)
        # return xxx
        print('exc1', self.host, self.port, self.db, self.charset,self.p1)

    def exc2(self):
        # conn = connect(host, port, db, charset)
        # conn.call_proc(sql)
        # return xxx
        print('exc2', self.host, self.port, self.db, self.charset,self.p2)



obj=excute('127.0.0.1',3306,'db1','utf8','a','b')
obj.exc1()
obj.exc2()
