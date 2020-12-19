# -*- coding: utf-8 -*-
'''=============================
#@Project : 基础
#@File    : eg03流程控制
#@Software: PyCharm
#@Author  : 某不知名代码搬运工
#@Email   : mnr6236784@163.com
#@Date    : 2020/6/24 22:52
#@Desc    : 第三部分程序流程控制
================================'''


# 12、根据输入的成绩数值（百分制），输出对应的等级，等级标准如下。
# 成绩在60以下：等级为D，成绩在60（含）到70之间：等级为C
# 成绩在70（含）到85之间：等级为B，成绩在85（含）以上：等级为A
def twelve():
    while 1:
        score = float(input("输入百分制成绩:"))
        if score >= 85:
            print('A')
            pass
        elif score >= 70:
            print('B')
            pass
        elif score >= 60:
            print('C')
            pass
        else:
            print('D')
            pass
        pass
    pass


# 13、计算1-100之间偶数的和，设置输出结果为整数，
# 宽度为8，居中对齐，空白处填充符号’*’。
def thirteen():
    sum1 = 0
    for i in range(0, 101, 2):
        sum1 = i+sum1
        pass
    print('{:*^8}'.format(str(sum1)))
    pass


# 14、计算1-2+3-4+….+99
def fourteen():
    a = 0
    b = 0
    for i in range(1, 100, 2):
        a = i+a
        pass
    for i in range(2, 100, 2):
        b = b-i
        pass
    print(a+b)
    pass


# 15、计算1到100中既能被3又能被5整除的数字的个数。
def fifteen():
    count0 = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            count0 += 1
            pass
        pass
    print('0-100既能被3又能被5整除的数的个数为:', count0)
    pass


# 16、输入n个数，输出其中的最小值。
def sixteen():
    st = input('输入n个数,以空格分隔:')
    lt = st.split(' ')  # 将字符串以空格分隔转为列表
    print(min(lt))  # 取最小值
    pass


# 17、输入一个字符串，计算分别其中小写字符、
# 大写字符、数字、其他字符的个数。
def seventeen():
    st = input("输入一个字符串:")
    big_count = 0
    small_count = 0
    digit_count = 0
    other_count = 0
    for s in st:
        if s.isupper():  # 大写
            big_count += 1
        elif s.islower():  # 小写
            small_count += 1
        elif s.isdigit():  # 数字
            digit_count += 1
        else:  # 其他字符
            other_count += 1
    print('大写:%d\n小写:%d\n数字:%d\n其他:%d'
          % (big_count, small_count, digit_count, other_count))
    pass


# 18、使用while循环计算1+2+3+…+100
def eighteen():
    bo = True
    i = 1
    a = 0
    while bo:
        a = a + i
        i += 1
        if i == 101:
            bo = False
            pass
        pass
    print(a)
    pass


# 19、输入一个正整数（位数不限），将其倒序输出，
# 如输入78961，输出16987；输入8900，输出0098。
def nineteen():
    st = input('输入一个正整数:')
    li = list(st)  # 字符串转列表
    li1 = list(reversed(li))  # 列表倒置
    st1 = ''
    st1 = st1.join(li1)  # 列表转字符串
    print(st1)
    pass


# 20、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13......，
# 计算它们的和，直到大于20为止，输出这期间至少需要累加多少个数。
def twenty01():
    n = int(input('生成前n项，请输入n的值:'))
    x = n
    li = [1, 2]
    sum0 = 0
    while n > 0:
        sum0 = sum0 + li[-1] / li[-2]
        print(li[-1])
        print(li[-2])
        print(li[-1] / li[-2])
        li.append(li[-1] + li[-2])
        n -= 1
        pass
    print('前%d项的和为:' % x, sum0)
    pass
twenty01()

def twenty02():  # 从第二个开始才有规律
    denominator = 1  # 分母
    denominator_temp = 1
    # 前两个相加
    print(denominator)
    for i in range(10):
        denominator, denominator_temp = denominator_temp + denominator, denominator  # 分母
        print(denominator)
    # 从第二个开始才有规律
    molecular = 2  # 分子
    molecular_temp = 1
    # 前两个相加
    print(molecular)
    for i in range(10):
        molecular, molecular_temp = molecular_temp + molecular, molecular  # 分母
        print(molecular)
    """求值代码"""
    denominator = 1  # 分母
    denominator_temp = 1
    molecular = 2  # 分子
    molecular_temp = 1
    total = 0
    while True:
        total += molecular / denominator
        molecular, molecular_temp = molecular_temp + molecular, molecular  # 分母
        denominator, denominator_temp = denominator_temp + denominator, denominator  # 分母
        print(f'总和{total} 计算：{molecular} / {denominator}')
        if total > 20:
            break
            pass


# 21、设计一个登录验证程序。输入用户名和密码，如果用户名和密码均正确，
# 输出“登录成功”并结束程序，否则输出“用户名或密码错误”的提示信息，
# 有3次输入错误的机会，如果超过3次登录错误，给出提示“3次输入错误，请稍后再试”。
def twenty1():
    import time
    default_name = 'roots'
    default_password = 'roots'
    count = 0
    while True:
        if count < 3:
            name = input("请输入用户名:")
            password = input("请输入密码:")
            if name == default_name and password == default_password:
                print("Welcome to Binary \n 登陆成功")
                break
                pass
            else:
                count += 1
                print("Error!Error!Error!")
                pass
            pass
        else:
            second = 0
            print("已错误三次，30秒后重试")
            for i in range(30):
                print('倒计时%d秒' % (30-second))
                time.sleep(1)
                second += 1
                pass
            count = 0
            pass
        pass

    pass


# 22、输入一组三位正整数，输入-1表示输入结束，输出这组数中水仙花数的个数。
# 水仙花数是这样一种数：它是三位正整数，它每个数位上的数的立方和等于它本身。
# 例如：153=13+53+33，所以153是一个水仙花数。
def twenty2():
    list0 = []
    count = 0
    # 得到除-1的列表
    while True:
        int1 = int(input('输入一组三位正整数，空格分隔，-1结束:'))
        if int1 != -1:
            list0.append(int1)
            pass
        else:
            break
            pass
        pass
    # 遍历列表得到水仙花数
    for i in list0:
        a = i // 100
        b = i % 100 // 10
        c = i % 10
        d = a ** 3 + b ** 3 + c ** 3
        if d == i:
            count += 1
            # print(i)
            pass
        pass
    # '100 200 300'.split(' ')  # 将以空格分隔的字符转列表
    print(list0)
    print('个数为:', count)
    pass


# 23、计算1！+2！+3！+…+10!
def twenty3():
    s = 1
    ss = 0
    for i in range(1, 101):
        for x in range(1, i+1):
            s = s*x  # 计算阶乘
            # print(s)
            pass
        ss = ss + s  # 求和
        s = 1  # 重新开始计算下一个数的阶乘
        pass
    print(ss)
    pass


# 24、请统计在某个给定范围[m, n]的所有整数中，
# 数字3出现的次数。在数字33中，3出现了2次。
def twenty4():
    n0 = int(input('输入范围下限:'))
    m0 = int(input('输入范围上限:'))
    str1 = ''
    for a in range(n0, m0+1):
        str1 = str1 + str(a)
        pass
    print(str1.count('3'))
    pass

