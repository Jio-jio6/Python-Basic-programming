# -*- coding: utf-8 -*-
'''=============================
#@Project : 基础
#@File    : eg01
#@Software: PyCharm
#@Author  : 某不知名代码搬运工
#@Email   : mnr6236784@163.com
#@Date    : 2020/6/22 13:35
#@Desc    : 第一部分简单数值计算
================================'''


import math


# 1、利用海伦公式计算三角形的面积（
# 对于不符合三角形两边和大于第三边规则的情况，要给出提示）。
# 海伦公式：三角形面积=√(p(p-a)(p-b)(p-c))，
# 其中a、b、c为三角形三边长，p为三角形周长的一半。


def hailun():
    while 1:
        a = float(input("输入a:"))
        b = float(input("输入b:"))
        c = float(input("输入c:"))
        if a+b <= c or a+c <= b or b+c <= a:
            print("不符合三角形任意两边和大于第三边的规则\n请重新输入")
            pass
        else:
            p = (a+b+c)/2
            s = math.sqrt(p*(p-a)*(p-b)*(p-c))
            print("该三角形面积为：", s)
            pass
        pass
    pass


# ==============================================
# 2、输入一元二次方程ax2 +bx+c=0的参数a、b、c，
# 计算并输出方程的实数根（结果保留两位小数）。
# 若方程没有实数根，输出“方程没有实数根”。
def er():
    while 1:
        print("请输入ax^2+bx+c=0的参数a、b、c")
        a = float(input("输入a:"))
        b = float(input("输入b:"))
        c = float(input("输入c:"))
        d = math.pow(b, 2)-4*a*c
        if d < 0:
            print("该方程无实根\n请重新输入")
            pass
        else:
            x1 = (-b + math.sqrt(d)) / 2 / a
            x2 = (-b - math.sqrt(d)) / 2 / a
            print("该方程的两个根为：", x1, "\n", x2)
            pass
        pass
    pass
	
	
# ======================================================
# 3、一只大象口渴了，要喝20升水才能解渴，但现在只有一个深h厘米，
# 底面半径为r厘米的小圆桶。问大象至少要喝多少桶水才会解渴。
# 输入两个整数（不考虑输入异常），分别表示小圆桶的深h和底面半径r，
# 单位都是厘米。输出一个整数，表示大象至少要喝水的桶数。
def water():
    # 1升=1000毫升=1000立方厘米
    h = float(input("输入圆筒深(cm):"))
    r = float(input("输入圆筒底面半径(cm):"))
    v = 3.1416*math.pow(r, 2)*h
    re = (20*1000) % v
    if re == 0:
        count = (20 * 1000) // v
        pass
    else:
        count = (20*1000)//v+1  # 取整+1
        pass
    print("最少需要喝%d桶水才能解渴" % count)
    pass
	
	
# ================================================
# 4、根据邮件的重量和用户是否选择加急计算邮费。计算规则：
# 重量在1000克以内(包括1000克), 基本费8元。超过1000克的部分，
# 每500克加收超重费4元，不足500克部分按500克计算。如果用户选择加急，多收5元。
# 输入一个整数表示重量（单位为克），输入一个字符表示是否加急。
# 如果字符是y，说明选择加急；如果字符是n，说明不加急。
# 输出一行，包含一个整数，表示邮费
def post():
    while True:
        ch = input("是否加急(y or n):")
        weight = int(input("请输入邮件重量(g):"))
        cost = 0
        if weight <= 1000:
            cost = 8
            pass
        else:
            s = (weight - 1000) % 500
            if s == 0:
                cost = (weight-1000)//500*4+8
                pass
            elif s != 0:
                cost = int((weight-1000)//500+1)*4+8
                pass
            pass
        if ch == "y":
            print("邮费为:", cost+5)
            pass
        elif ch == "n":
            print("邮费为:", cost)
            pass
        pass
    pass


# ==================================================
# 5、将一个三位正整数取反向输出反义词
def antonym():
    while True:
        d = int(input("输入一个三位正整数:"))
        a = d // 100
        b = d % 100 // 10
        c = d % 10
        e = c*100+b*10+a
        print("该整数的反向输出结果是:", e)
        pass
    pass
	
	
# ==================================================
# 6、李老师购买了一批铅笔，平均分给班级中的同学，
# 输入铅笔数量和班级学生人数，计算并输出每人分得几只铅笔，余几只

def avg():
    while True:
        pen = int(input("铅笔数量:"))
        stu = int(input("学生数量:"))
        ag = pen // stu
        re = pen % stu
        print("每人分到%d支铅笔" % ag)
        print("余%d支铅笔" % re)
        pass
    pass
	
	
# ==========================================
# 7、输入一个整数，输出该数是“奇数”还是“偶数”。
def num():
    while True:
        n = int(input("输入一个整数:"))
        if n % 2 == 0:
            print("是偶数")
            pass
        else:
            print("是奇数")
            pass
        pass
    pass


