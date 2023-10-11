# _*_coding:utf-8 _*_

#@Time      : 2021/12/16  0:03
#@Author    : An
#@File      : test222.py
#@Software  : PyCharm

try:
    a = int(input('请输入一个被除数'))
    b = int(input('请输入除数'))
    c = float(a)/float(b)
    print(c)
except ZeroDivisionError:
    print('异常，被除数不能为零')
except ValueError:
    print('异常，不能输入字符串！')
except NameError:
    print('异常，变量不存在！')

except BaseException as e:
    print(e)