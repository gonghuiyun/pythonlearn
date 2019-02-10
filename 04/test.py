'''
练习，利用b模式，编写一个cp工具，要求如下：
　　1. 既可以拷贝文本又可以拷贝视频，图片等文件
　　2. 用户一旦参数错误，打印命令的正确使用方法，如usage: cp source_file target_file
　　提示：可以用import sys，然后用sys.argv获取脚本后面跟的参数
'''
'''
import sys
if len(sys.argv) != 3:
    print('usage: cp source_file target_file')
    sys.exit()

source_file,target_file=sys.argv[1],sys.argv[2]
with open(source_file,'rb') as read_f,open(target_file,'wb') as write_f:
    for line in read_f:
        write_f.write(line)
'''
import sys
if len(sys.argv)!=3:
    print('usage: cp source_file target_file')
    sys.exit()
source,target=sys.argv[1],sys.argv[2]
with open(source,'rb') as fsour,open(target,'wb') as ftar:
    data=fsour.read()
    ftar.write(data)