# -*- coding: utf-8 -*-
'''=============================
#@Project : 基础
#@File    : eg02
#@Software: PyCharm
#@Author  : 某不知名代码搬运工
#@Email   : mnr6236784@163.com
#@Date    : 2020/6/23 13:40
#@Desc    : 第二部分字符串操作
================================'''


import re


# 8、给定字符串s1=" my python program  "，
# 利用字符串操作符即字符串处理函数完成下列操作：
# （1）去掉字符串s1首尾空格
# （2）字符串长度
# （3）字符串大小写转换
# （4）字符串的索引和查找函数
# （5）字符串切片
# （6）字符串的拆分与合并函数
def eight():
    s = "   my python program   "
    s1 = s.strip()  # strip()函数去除字符串首尾空格
    print("==1out==")
    print(s, '\n', s1)
    c2 = len(s)
    print("==2out==")
    print(c2)
    print("==3out==")
    s3 = s1
    print(s3.upper())  # 把所有字符中的小写字母转换成大写字母
    print(s3.lower())  # 把所有字符中的大写字母转换成小写字母
    print(s3.capitalize())  # 把第一个字母转化为大写字母，其余小写
    print(s3.title())  # 把每个单词的第一个字母转化为大写，其余小写
    print("==4out==")
    print(s1.find('a'))  # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：15
    print(s1.find('a', 1))  # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
    print(s1.find('333'))  # 查找不到返回-1
    print(s1.index('a'))
    print(s1.index('y'))  # 找不到不会返回-1而是抛出异常
    print("==5out==")
    # 格式： [start: end:step]
    #  [:] 提取从开头（默认位置0）到结尾（默认位置 - 1）的整个字符串
    #  [start:] 从start提取到结尾
    #  [: end] 从开头提取到end - 1
    #  [start: end] 从start提取到end - 1
    # [start: end:step] 从start提取到end - 1，每step个字符提取一个
    #  左侧第一个字符的位置 / 偏移量为0，右侧最后一个字符的位置 / 偏移量为 - 1
    print(s1[2::2])
    print(s1.split(' '))  # 依据空格切割得到单词
    # 根据正则表达式提取字符串中的单词
    s5 = re.compile(r'\b[a-zA-Z]+\b', re.I).findall(s1)
    print(s5)
    print("==6out==")
    s6 = 'hello '
    print(s6+s1)
    pass

	
# 9、编写一个温度转换程序。将用户输入华氏温度转换为摄氏温度，
# 或将输入的摄氏温度转换为华氏温度。要求输入输出的摄氏温度采用字母C开头、
# 华氏温度采用字母F开头，如C12指摄氏度12度，F87.65指华氏度87.65度，
# 不考虑输入异常的情况；输出结果保留小数点后两位。
# 转换算法如下：（C表示摄氏度、F表示华氏度）
# C = ( F - 32 ) / 1.8
# F = C * 1.8 + 32
def nine():
    while 1:
        ch = input("华氏度(F)摄氏度(C),F or C ?:")
        ch1 = ch[0]  # 得到F或C
        tem = float(ch[1:])  # 得到数字
        try:
            if ch1 == 'C':
                result0 = tem * 1.8 + 32
                print('%.2f' % result0)
                pass
            elif ch1 == 'F':
                result0 = (tem - 32) / 1.8
                print('%.2f' % result0)
                pass
        except BaseException:
            print('输入有错误！请重新输入！')
            pass
        pass
    pass

	
# 10、给定一个只包括字符和空格的句子，将句子中的单词位置反转后输出。
# 输入的句子占一行，各个单词之间以空格分隔。例如，
# 输入this is a test，输出 test a is this。
# 提示：本题采用的方法是将输入的字符串分隔，
# 转换为列表，将列表反转后再生成字符串输出。
def ten():
    str1 = input("输入英文句子，以空格分隔:")
    list1 = str1.split(' ')  # 将字符串以空格分隔
    print(list1)
    list2 = list(reversed(list1))  # 将列表倒置
    print(list2)
    rst = ''
    for i in list2:
        rst = rst+' '+i
        pass
    print(rst)
    pass

	
# 11、输入一个字符串表示某员工一周5天的出勤情况，形式为AppaL，
# 其中A(大小写均可)表示缺勤，L(大小写均可)表示迟到，
# P(大小写均可)表示出勤，如果不大于一次缺勤且不超过两次迟到，
# 输出“合格”，否则输出“不合格”。
from collections import Counter
def eleven():
    print('输入五天出勤情况A(缺勤)P(出勤)L(迟到)')
    state1 = input('输入格式如(ApPlp):')
    state2 = state1.lower()  # 统一转成小写字母
    a_count = state2.count('a')  # 缺勤次数
    l_count = state2.count('l')  # 迟到次数
    p_count = state2.count('p')  # 出勤次数
    dict1 = Counter(state2) #统计字符串每个字符出现次数，返回字典
    # 最少保证三天出勤则合格
    if p_count >= 3 and a_count < 2:
        print('合格')
        pass
    else:
        print('不合格')
        pass
    pass


eleven()





