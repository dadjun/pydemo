#!usr/bin/python
# -*- coding: utf-8 -*-


import math
from basic.timedemo import printcurTime

printcurTime()
content = dir(math)
print(content)

str1 = "ts1323"
def funcStrTest():
    print('#----------字符串-------------------\n')

    global str1
    str1 = 'dadjun'
    print(str1)
    print(str1[0:-1])
    print(str1[0:-3])
    print(str1[2:4])
    print(str1 *2 )
    print('hello \ndadjun')
    print(r'hello \ndadjun')

funcStrTest()

def funcCollectionDemo():
    print('#----------元组、集合、转换-------------\n')
    var1 = 10
    list0 = list('12495637')
    list0.sort()
    print(list0)
    print(tuple('67666'))#tuple元组不能修改，list能修改
    tup1 = tuple('56789')
    list1 = list(tup1)
    list1.reverse()
    print(list1)
    for i in range(len(list1)):
        print(list1[i])
    print('#----------集合------------------\n')
    dic = {'key1': 1, 'key1': 1, 2: 'ada', 'key3': 3}
    dic[2] = 168
    print(dic[2])

def funcMathDemo():
    var2 = math.floor(2.3)
    var3 = str(var2)
    print(repr(var2))
    print('math' +var3 )
    #aa = input('\n\n please input words')
    print(math.pi)

def funcLogicDemo():
    print('#----------循环条件判断------------------\n')
    n = 10
    sum = 0
    counter = 1
    while counter <= n:
        sum = sum + counter
        counter += 1
    print("1到%d之和wei%d",n,sum)

    lang = 'java'
    flag = True
    if lang == 'python':
        flag = False
        print(lang)
    elif lang == 'java':
        flag = True
        print(lang)
    else:
        flag = False
        print(lang)
    print(flag)
    num = 10
    if num < 10 or num > 10:
        print('hello')
    else:
        print('undefine')

def funcListDemo():
    print('#----------函数------------------\n')
    fruits = ['banana','apple','orange']
    fruits.append('mango')

    for fruit in ((fruits)):
        print('当前水果'+ fruit)

    for index in range(len(fruits)):
        print('当前水果用iterator'+ fruits[index])

def printme(str='默认打印哈哈'):
    "打印任何传入的字符串"
    print(str)
    return 'printed'

printme('不打哈哈，打印我')

def functionname(arg1, *vartuple):
   "函数_文档字符串"
   print("输出: ")
   print(arg1)
   for var in vartuple:
       print(var)
   return

functionname(12,2,321,675)


