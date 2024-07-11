# a_list=['a', 'b', 'mpilgrim', 'z', 'example']
# for i in range(len(a_list)):
#     print('列表第',i,'个元素是',a_list[i])
# for k,v in enumerate(a_list):
#     print('列表第',k,'个元素是',v)
# al = ['a', 'b', 'mpilgrim', 'z', 'example']
# bl = al.copy() #bl是al的一个别名,操作bl相当于操作al
# bl[0]='123'
# print(al)
# x=[1,2,1,2,1,1,1]
# for i in x[::]:
#     if i==1:
#         x.remove(i)
# print(x)
# a_dict=dict.fromkeys(['name','age','sex'],'default')
# print(a_dict.get('abs',456))
# x=[1,2,3,4]
# x.pop()
# 姓名='王奕澄'
# print(姓名)
# pp="My name is {name},my age is {age:d},and my QQ is {qq:d}".format(name="Wang Yicheng",age=20,qq=100)
# print(pp)
# for j in range(1,9):
#     line=[]
#     for i in range(1,j+1):
#         line.append("{}*{}={}".format(i,j,i*j))
#     print(line)
#
# s = "apple,peach,banana,pear"
# a,b,c,d=s.split(',')
# print(a,b,c,d)
# e=','.join(s)
# print(e)
from newPackage.hello import *  # from 包.模块（也就是文件名） import 方法（也就是函数名）

# import requests

hello()
