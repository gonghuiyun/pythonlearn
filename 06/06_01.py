def menu_cre(name,menu):
    for i, j in menu.items():
        if i == name:
            menu_next = menu[name]
    return menu_next
def keys_list(menu):
    l_k = []
    k1 = menu.keys()
    for i in k1:
        l_k.append(i)
    return l_k
def menu_pri(layer,l1,l2,l3):
    if layer==1:
        print(l1)
    elif layer==2:
        print(l2)
    else:
        print(l3)
def find_layer(name):
    if name in l1:
        layer_flag=1
    elif name in l2:
        layer_flag=2
    else:
        layer_flag=3
    return layer_flag
def last_layer(layer):
    if layer==1:
        print('this is root menu')
        return False
    else:
        return layer-1
#create menu
menu1 = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '电子厂':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

menu2=menu_cre('北京',menu1)
menu3=menu_cre('海淀',menu2)
#create key list
l1=keys_list(menu1)
l2=keys_list(menu2)
l3=keys_list(menu3)
print(l1,l2,l3)
Tag1=True
Tag2=True
while Tag1:
    name_place = input('please input place name: ').strip()
    layer=find_layer(name_place)
    menu_pri(layer,l1,l2,l3)
    while Tag2:
        re_flag = input('return last layer?(Y/N): ')
        if re_flag == 'Y':
            if last_layer(layer):
                layer=last_layer(layer)
                menu_pri(layer,l1,l2,l3)
                exit_code = input('exit?(Y/N): ')
                if exit_code == 'Y':
                    Tag1 = False
                    Tag2 = False
                else:
                    continue
            else:
                break
        else:
            exit_code=input('exit?(Y/N): ')
            if exit_code=='Y':
                Tag1=False
                Tag2=False
            else:
                Tag2=False
    continue


