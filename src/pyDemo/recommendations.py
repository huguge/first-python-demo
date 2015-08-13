#coding=utf-8
'''
Created on 2015年8月13日

利用用户对电影的评价来推断用户之间的相似度
'''

from math import sqrt

# 用户对电影的评论分数
critics = {'Lisa Rose':{'Lady in the Water':2.5, 'Snakes on a Plane':3.5, 'Just My Luck':3.0, 'Superman returns':3.5,
    'You, Me and Dupree':2.5, 'The Night Listener':3.0},
'Gene Seymour':{'Lady in the Water':3.0, 'Snakes on a Plane':3.5, 'Just My Luck':1.5, 'Superman returns':5.0,
    'The Night Listener':3.0, 'You, Me and Dupree':3.5},
 'Michael Phillips':{'Lady in the Water':2.5, 'Snakes on a Plane':3.0, 'Superman returns':3.5, 'The Night Listener':4.0},
'Claudia Puig':{'Snakes on a Plane':3.5, 'Just My Luck':3.0, 'The Night Listener':4.5, 'Superman returns':4.0,
    'You, Me and Dupree':2.5},
'Mick Lasalle':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0, 'Just My Luck':2.0, 'Superman returns':3.0, 'The Night Listener':3.0,
    'You, Me and Dupree':2.0},
'Jack Matthews':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0, 'The Night Listener':3.0, 'Superman returns':5.0,
    'You, Me and Dupree':3.5},
'Toby':{'Snakes on a Plane':4.5, 'You, Me and Dupree':1.0, 'Superman returns':4.0}        
         }

# 返回一个有关 person1 与 person2 的基于距离的相似度评价
def sim_distance(prefs,person1,person2):
    # 得到 share_items 的列表
    si = {}
    for item in prefs[person1]:# 循环person1 评价的影片
        if item in prefs[person2]:# 如果person1 评价的影片在 person2 评价的影片中
            si[item] = 1
    
    # 如果两者没有共同之处，则返回0
    if len(si) == 0:return 0
    
    # 计算所有差值的平方和
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sqrt(sum_of_squares))

# 输出两个用户的相似度，越接近  1 则越相似
print sim_distance(critics, 'Lisa Rose', 'Gene Seymour')