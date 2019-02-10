age = input('your age>>:')
if age.isdigit():
    age_int=int(age)
    age_int +=1
    print(age_int)
else:
    print(age)