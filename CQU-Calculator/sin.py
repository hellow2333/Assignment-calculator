##########
# 小组成员：季宇成、孔保元、胡锦杰、余澳
# 程序说明：定义SIN函数
# 完成人：季宇成
##########

from math import fabs
from math import pi

def sin(x):
    """
    :param x: 输入参数为角度值
    :return: x的正弦值
    """
    x = x / 180 * pi    # 输入角度转换为弧度
    g = 0
    t = x
    n = 1

    # 使用泰勒展开式对sin值进行计算
    while fabs(t) >= 1e-15:   # 设置计算的精度
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return round(g, 10)  # 计算结果保留十位小数

# test 测试代码
"""
ans1 = sin(60)
print("sin（60°）=", ans1)
ans2 = sin(45)
print("sin（45°）=", ans2)
ans3 = sin(30)
print("sin（30°）=", ans3)
"""