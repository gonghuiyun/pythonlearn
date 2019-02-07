'''
 用户名，密码和余额存放于文件中，格式为：Albert|Albert123|3000
    启动程序后：
        已注册用户===>先登录===>登录成功===>读取用户余额===>开始购物
                     登录过程中，用户密码输入超过三次则退出程序,
                     并将用户名添加到黑名单，再次启动程序登陆改用户名，提示用户禁止登陆
        未注册用户===>先注册===>注册成功===>输入用户工资，即为用户余额===>开始购物
                     注册过程中，用户密码输入两次一样才可以注册
    允许用户根据商品编号购买商品，比如：
        1 iPhone
        2 mac book
        3 bike
    用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    可随时退出，退出时，打印已购买商品和余额
'''
import sys
def login(dict):
    count=0
    print('please login your account')
    name_login = input('input user name: ')
    password = input('input your password: ')
    while (password!=dict[name_login]):
        password = input('input your password: ')
        count=count+1
        if count==2:
            print('you are forbidden')
            with open('forbi.txt','a') as f_forbi:
                f_forbi.write('\n')
                f_forbi.write(name_login)
            sys.exit()
    return True,name_login
def register():
    name_login = input('set your register name: ')
    password1 = input('set your password: ')
    password2 = input('set your password again: ')
    if password1==password2:
        salary = input('set your salary: ')
        with open('usrifo.txt','a') as f_usrifo:
            f_usrifo.write('\n')
            f_usrifo.write(name_login)
            f_usrifo.write('|')
            f_usrifo.write(password1)
            f_usrifo.write('|')
            f_usrifo.write(salary)
    else:
        print('two password don \\\'t consistent!')
        sys.exit()
#read usr information file
def read_ifo():
    l = []
    dict_info = {}
    with open('usrifo.txt', 'r') as f_ifo:
        for line in f_ifo:
            l = line.split('|')
            print(dict_info)
            dict_info[l[0]] = l[1]
    return dict_info
def read_salary():
    l = []
    dict_info = {}
    with open('usrifo.txt', 'r') as f_ifo:
        for line in f_ifo:
            l = line.split('|')
            dict_info[l[0]] = l[2]
    return dict_info
def buy_l():
    l=[]
    tag=True
    while tag:
        exit_l_flag=input('continue buy?(Y/N): ')
        if exit_l_flag =='Y':
            l.append(input('input goods number: '))
        else:
            tag=False
    return l
#login
Tag=False
regist_flag=input('do you have account?(Y/N): ')
if regist_flag == 'Y':
    login_fla,log_name=login(read_ifo())
    if login_fla:
        Tag=True
else:
    register()
    login_fla, log_name = login(read_ifo())
    if login_fla:
        Tag=True
#buy goods
salary=int(read_salary()[log_name])
goods = {'1': ['iPhone', 5000],
             '2': ['mac book', 10000],
             '3': ['bike', 300],
             }

while(Tag):
    buy_list = buy_l()
    pay = 0
    for i in buy_list:
        pay = pay + goods[str(i)][1]
    if pay > salary:
        print('pay failed: money is not enough!')
        exit_flag = input('exit?(N/Y): ')
        if exit_flag=='Y':
            sys.exit()
        else:
            buy_list.clear()
            continue
    else:
        for i in buy_list:
            print(goods[str(i)][0])
        print(salary - pay)
        sys.exit()
