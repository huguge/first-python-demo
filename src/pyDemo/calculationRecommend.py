#coding=utf-8
'''
Created on 2015年8月13日

@author: 80s
'''
# from math import sqrt
# print sqrt(pow(4.5-4, 2)+pow(1-2, 2))
# 
# 
# print 1/(1+sqrt(pow(4.5-4, 2)+pow(1-2, 2)))

from math import sqrt
# 返回一个有关 person1 与 person2 的基于距离的相似度评价
def sim_distance(prefs,person1,person2):
    # 得到 share_items 的列表
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    
    # 如果两者没有共同之处，则返回0
    if len(si) == 0:return 0
    
    # 计算所有差值的平方和
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2)]
                         for item in prefs[person1] if item in prefs[person2])
    
    return 1/(1+sqrt(sum_of_squares))