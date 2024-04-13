##########
# 小组成员：季宇成、孔保元、胡锦杰、余澳
# 程序说明: 测试函数
##########

import math
from asin import asin
from atan import atan
from cos import cos
from sin import sin

###  测试部分，显示误差大小，以及math库中计算的结果和自己的结果
def test_sin(x):
    math_sin_value = math.sin(math.radians(x))

    custom_sin_value = sin(x)
    # 计算两者之间的误差
    err = abs(math_sin_value - custom_sin_value)
    print('sin功能两者误差(值)为err=', err)
    print('Python中math.sin(%d)=%f' % (x, math_sin_value))
    print('自己实现的sin(%d)=%f' % (x, custom_sin_value))

def test_cos(x):
    math_cos_value = math.cos(math.radians(x))

    custom_cos_value = cos(x)
    # 计算两者之间的误差
    err = abs(math_cos_value - custom_cos_value)
    print('cos功能两者误差(值)为err=', err)
    print('Python中math.cos(%d)=%f' % (x, math_cos_value))
    print('自己实现的cos(%d)=%f' % (x, custom_cos_value))

def test_arcsin(x):
    math_asin_value = math.degrees(math.asin(x))

    custom_asin_value = asin(x)
    # 计算两者之间的误差
    err = abs(math_asin_value - custom_asin_value)
    print('arcsin功能两者误差(值)为err=', err)
    print('Python中math.asin(%d)=%f' % (x, math_asin_value))
    print('自己实现的asin(%d)=%f' % (x, custom_asin_value))

def test_arctan(x):
    math_atan_value = math.degrees(math.atan(x))

    custom_atan_value = atan(x)
    # 计算两者之间的误差
    err = abs(math_atan_value - custom_atan_value)
    print('arctan功能两者误差(值)为err=', err)
    print('Python中math.atan(%d)=%f' % (x, math_atan_value))
    print('自己实现的atan(%d)=%f' % (x, custom_atan_value))

if __name__ == '__main__':
    print("测试30°的sin和cos值：")
    test_sin(30)
    test_cos(30)
    print("\n测试45°的sin和cos值：")
    test_sin(45)
    test_cos(45)

    print("\n测试0.5的arcsin")
    test_arcsin(0.5)

    print("\n测试0.75的arcsin")
    test_arcsin(0.75)

    print("\n测试1的arctan值：")
    test_arctan(1)

    print("\n测试5的arctan值：")
    test_arctan(5)
    # while True:
    #     x=input("请输入测试函数(如格式：sin、cos、arcsin、arctan）:")
    #     if x=='sin':
    #         y=float(input("请按要求输入数字："))
    #         test_sin(y)
    #         z=input("continue?(y/n):")
    #         if z=='n'or z=='N':  # 即使条件是 z == 'n' or 'N'，它也会被解释为真
    #             break
    #     elif x=='cos':
    #         y=float(input("请按要求输入数字："))
    #         test_cos(y)
    #         z=input("continue?(y/n):")
    #         if z=='n'or z=='N':
    #             break
    #     elif x=='arcsin':
    #         y=float(input("请按要求输入数字："))
    #         test_arcsin(y)
    #         z=input("continue?(y/n):")
    #         if z=='n'or z=='N':
    #             break
    #
    #     elif x=='arctan':
    #         y = float(input("请按要求输入数字："))
    #         test_arctan(y)
    #         z = input("continue?(y/n):")
    #         if z == 'n' or z == 'N':
    #             break