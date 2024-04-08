##########
# 小组成员：季宇成、孔保元、胡锦杰、余澳
# 程序说明：定义cos函数
# 完成人： 孔保元
##########

from math import pi

def cos(x):
    """
    :param x: 输入参数为角度值
    :return: x的余弦值
    """
    return round(taylor(x, 50), 10)

def factorial(a):    # 阶乘
    b = 1
    while a != 1:
        b *= a
        a -= 1
    return b

def taylor(x, n):
    a = 1
    x = x/180 * pi    # 转换为弧度
    count = 1
    for k in range(1, n):
        if count % 2 != 0:
            a -= (x**(2*k))/factorial(2*k)
        else:
            a += (x**(2*k))/factorial(2*k)
        count += 1
    return a

# test 测试代码
"""
ans1 = cos(60)
print("cos（60°）=", ans1)
ans2 = cos(45)
print("cos（45°）=", ans2)
ans3 = cos(30)
print("cos（30°）=", ans3)
"""