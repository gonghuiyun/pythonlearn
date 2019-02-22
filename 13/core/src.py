# import sys,os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

import json
import time
from conf import settings
from lib import common
logger = common.get_logger(__name__)

# 用户信息
dic = common.conn_db()
# 商品信息
dic_com = common.conn_com()
# 登录标志
login_flag = False

# 先判断是否有此用户，若有，则登录;若无，则先注册再登录
def login_final(func):
    def tmp():
        global dic
        name = input('Please input your name >> ')
        if name not in dic.keys():
            print('Please register!')
            logger.info('Register')
            name = input('Please set login name >> ')
            password = input('Please set your password >> ')
            money = input('Please set your money >> ')

            dic[name]={"password": password, "money" : int(money)}
            with open(BASE_DIR+'/db/db.json', 'w') as f:
                j=json.dump(dic, f)
            res=func()
        else:
            logger.info('login')
            res=func()
        return res
    return tmp


# 检测密码是否与用户名匹配，若匹配成功，则login_flag为True，
# 否则重新输入密码，超过3次自动退出程序
@login_final
def login():
    global dic
    global  login_flag
    #print('Please login!')

    name = input('Please input your name >> ')
    count = 0
    while True:
        if count>2:
            logger.info('Login error')
            print('please login again!')
            return
        else:
            password = input('Please input password >> ')
            if not dic[name]['password'] == password:
                count+=1
                continue
            else:
                login_flag=True
                return name


# 输入一种商品的序号，输出商品名称，价格
def get_price(index):
    global dic_com
    for i,j in dic_com.items():
        if int(i) == index:
            for k, h in j.items():
                return k, h

# 输入商品序号，购买数目，返回总价
def buy_one(index, count):
    _, price=get_price(index)
    price=price * count
    return price

# 输入用户名，返回余额
def usr_res(name):
    dic = common.conn_db()
    return dic[name]['money']

def change_res(name, price):
    dic = common.conn_db()
    dic[name]['money'] = price
    with open(BASE_DIR + '/db/db.json', 'w') as f:
        j = json.dump(dic, f)

# 形成购买清单
def buy_list(name):
    l=[]
    while True:
        flag_exit = input('continue?(Y/N) >> ')
        if flag_exit == 'N':
            logger.info('Exit')
            break
        else:
            logger.info('Choice commodity')
            index = input('Please input good index >> ')
            count = input ('Please input good number >> ')
            name_good,_ = get_price(int(index))
            price = buy_one(int(index),int(count))

            dic_buy={'name': name_good,
                     'count': count,
                     'price': price
                    }

            origin = usr_res(name)
            if origin-price > 0:
                change_res(name, origin-price)
                l.append(dic_buy)
                logger.info('Buy success!')
            else:
                logger.info('Buy error: money not enough')
                print('money not enough!')
                continue
    if len(l)>0:
        print(l)
    else:
        print('buy nothing!')

# 先登录，若用户名不存在则注册后登录，登录成功后购买商品，最后打印购买的商品信息
def process():
    global login_flag
    while True:
        if not login_flag:
            name = login()
        else:
            buy_list(name)
            print('信用卡余额： ',usr_res(name))
            return

#if __name__ == '__main__':

process()



