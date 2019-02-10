count=0
age_pre=20
while(True):
    age=input('please input age: ')
    if int(age)==age_pre:
        break
    else:
        count=count+1
    if count==3:
        ask=input('continue?(Y/N)')
        if ask=='Y':
            count=0
            continue
        else:
            break
print('game is over')