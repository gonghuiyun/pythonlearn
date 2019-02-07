'''
练习，利用b模式，编写一个cp工具，要求如下：
　　1. 既可以拷贝文本又可以拷贝视频，图片等文件
　　2. 用户一旦参数错误，打印命令的正确使用方法，如usage: cp source_file target_file
　　提示：可以用import sys，然后用sys.argv获取脚本后面跟的参数
'''
import sys
#while(True):
ori=input('original: ').strip()
tar=input('target: ').strip()
sys.argv.append(ori)
sys.argv.append(tar)

with open(sys.argv[1], 'rb') as fori, open(sys.argv[2], 'wb') as ftar:
    data=fori.read()
    ftar.write(data)
'''
    for line in fori:
        ftar.write(line)
'''
'''
    if len(sys.argv)!=3:
        print('Input error!')
        flag=input('continue? Y/N ')
        if flag=='Y':
            continue
        else:
            break
    elif len(sys.argv)==3:

    sys.exit()
'''
'''
import sys


source_address = input('请输入被拷贝文件源地址: ').strip()
target_address = input('请输入拷贝文件目标地址: ').strip()
sys.argv.append(source_address)
sys.argv.append(target_address)


#source_file,target_file=sys.argv[1],sys.argv[2]

with open(sys.argv[1],'rb') as read_f,open(sys.argv[2],'wb') as write_f:
    for line in read_f:
        write_f.write(line)
'''