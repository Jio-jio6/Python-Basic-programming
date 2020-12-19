# -*- coding: utf-8 -*-
'''=============================
#@Project : 基础
#@File    : eg04组合数据类型
#@Software: PyCharm
#@Author  : 某不知名代码搬运工
#@Email   : mnr6236784@163.com
#@Date    : 2020/7/1 23:48
#@Desc    : 第四部分组合数据类型
================================'''


# 25、输入一组整数，存储在列表中，遍历输出列表元素。
def twenty5():
    list1 = input('输入一组整数，空格分隔:').split(' ')
    print(list1)
    for i in list1:
        print(i, end=' ')
        pass
    pass


# 26、输入一组数字，在一行输入，数字之间以空格分隔，
# 计算这组数字的最大值（计算这组数字的平均值）。
def twenty6():
    a = 0
    list1 = input('输入一组整数，空格分隔:').split(' ')
    print(max(list1))
    for i in list1:
        a = a+float(i)
        pass
    print(a/len(list1))
    pass


# 27、利用简单选择排序的方法，将一个列表中的10个数按从小到大的顺序排列。
# 对于n个数，简单选择排序的基本思想是，求出第1个到最后1个数中的最小值，
# 将最小值与第1个数互换；求出第2个到最后1个数中的最小值，将最小值与第2个数互换；
# 以此类推。选择法排序的每次循环，都使1个数放置在正确的位置。
def twenty7():
    arr = input('空格分隔：').split()
    print(arr)
    list01 = []
    for i in arr:
        list01.append(float(i))
        pass
    print(list01)
    # 求出arr的长度
    n = len(list01)
    # 外层循环确定比较的轮数，x是下标，arr[x]在外层循环中代表arr中所有元素
    for x in range(n - 1):
        # 内层循环开始比较
        for y in range(x, n):
            # arr[x]在for y 循环中是代表特定的元素，arr[y]代表任意一个arr任意一个元素。
            if list01[x] > list01[y]:
                # 让arr[x]和arr列表中每一个元素比较，找出小的
                list01[x], list01[y] = list01[y], list01[x]
    print(list01)
    pass


# 28、给定一个有10个整数的列表，输出其中的最大值以及最大值在列表中的索引。
def twenty8():
    arr1 = input('空格分隔：').split()
    list02 = []
    for i in arr1:
        list02.append(float(i))
        pass
    list02.sort()
    print("升序:", list02)
    list02.sort(reverse=True)
    print("降序:", list02)
    pass


# 29、给定三个3×3矩阵，存储在列表a中（a=[[1,2,3],[4,5,6],[7,8,9]]），
# 输出矩阵元素，并输出矩阵的主对角线（从左上角到右下角）的元素之和。矩阵的输出形式如下：
# 1	2	3
# 4	5	6
# 7	8	9
# 主对角线元素和为1+5+9=15
def twenty9():
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    s = 0
    count1 = 0
    for i in a:
        # print(i)
        for y in i:
            print(y, end='  ')
            pass
        print('')
        s = i[count1] + s
        count1 += 1
        pass
    print(s)
    pass


# 30、学校要选取一部分同学参与一项问卷调查，通过生成n个1-1000之间没有重复的
# 随机整数的方式随机抽取学生，每个随机整数对应不同的学生学号，请编写程序，
# 输入参与调查的学生人数，按从大到小的顺序输出生成的学生学号。
# random.randint(1,1000)函数生成1到1000之间的随机整数，返回值为int型
def thirty():
    import random
    x = int(input('输入人数：'))
    list3 = []
    for i in range(x):
        a = random.randint(1, 1000)
        list3.append(a)
        pass
    list3.sort(reverse=True)
    print(list3)
    pass


# 31、建立字典 dict，包含内容是："数学":"L04","语文":"W01","英语":"W02",
# "物理":"L02","地理":"Q03"。完成下列操作：
# （1）向字典中添加键值对"化学":"L03"。（2）修改"数学"对应的值为"L01"。
# （3）删除"地理"对应的键值对。（4）按如下格式打印字典dict全部信息。
# L01:数学
# W01:语文
# W02:英语
# L02:物理
# L03:化学
def thirty1():
    dict0 = {"数学": "L04", "语文": "W01", "英语": "W02",
             "物理": "L02", "地理": "Q03"}
    dict1 = dict0  # 拷贝
    dict1["化学"] = "L03"
    print(dict1)
    dict1["数学"] = "L01"
    print(dict1)
    del dict1["地理"]
    print(dict1)
    k1 = dict1.keys()  # 取键
    v1 = dict1.values()  # 取值
    dict2 = dict(zip(v1, k1))  # 键值互换生成新的字典
    print(dict2)
    for i in dict2:
        print(i, dict2[i])
        pass
    pass


# 32、输入一组学生的学号和成绩，以学号为key，以成绩为value，存放在字典中（
# 每输入一个学生信息，提示是否继续输入（y/n），y为继续输入，n为结束输入），
# 按学号升序输出学生信息，输出形式为
# 学号：成绩
def thirty2():
    dict1 = {}
    while True:
        str0 = input('输入（y/n）：')
        if str0 == 'y':
            num = int(input('输入学号：'))
            sco = float(input('输入成绩：'))
            dict1[num] = sco
            pass
        elif str0 == 'n':
            break
            pass
        else:
            print('错误输入，请重试')
            pass
        pass
    # by_key = sorted(dict1.items(), key=lambda item: item[0])  # 按照键排序
    # by_value = sorted(dict1.items(), key=lambda item: item[1])  # 按照值排序
    # print(by_key, type(by_key))
    for each in sorted(dict1):
        print(each, ':', dict1[each])
        pass
    pass

