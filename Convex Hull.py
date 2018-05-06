# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:15:28 2018

@author: XIN
"""

import random
import matplotlib.pyplot as plt
import operator
import math

def gen_points(n):
    res = []
    for i in range(n):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        res.append((x, y))
    return res

def find_split(points):
    points.sort(key=lambda x: x[0], reverse=False)
    l = len(points)
    if l == 0:
        return None
    else:
        return 0.5 * (points[l//2-1][0] + points[l//2][0])

def split_points(points, split):
    splitA = []
    splitB = []
    for point in points:
        if point[0] < split:
            splitA.append(point)
        else:
            splitB.append(point)
    return splitA, splitB

def arrange_CW(points):
    l = len(points)
    mean_X = 0
    mean_Y = 0
    for i in range(l):
        mean_X += points[i][0] / l
        mean_Y += points[i][1] / l
    points.sort(key=lambda x: math.atan2(x[1]-mean_Y, x[0]-mean_X), reverse=True)
    X_min_index, X_min_coord = min(enumerate(points), key=lambda x: x[1][0])
    start_point = points.index(X_min_coord)
#    print(X_min_coord)
    points = points[start_point:] + points[:start_point]
    return points
    
def arrange_CCW(points):
    l = len(points)
    mean_X = 0
    mean_Y = 0
    for i in range(l):
        mean_X += points[i][0] / l
        mean_Y += points[i][1] / l
    points.sort(key=lambda x: math.atan2(x[1]-mean_Y, x[0]-mean_X), reverse=False)
    X_max_index, X_max_coord = max(enumerate(points), key=lambda x: x[1][0])
    start_point = points.index(X_max_coord)
#    print(X_max_coord)
    points = points[start_point:] + points[:start_point]
    return points    

def intersection(point1, point2, split):
    return (point2[1]-point1[1])/(point2[0]-point1[0]) * split - (point2[1]-point1[1])/(point2[0]-point1[0]) * point2[0] + point2[1] 
def merge(CH_A, CH_B, split):
    CH = []
    iA = 0
    iB = 0 
    CH_A = arrange_CCW(CH_A)
    CH_B = arrange_CW(CH_B)
    intersect = intersection(CH_A[iA], CH_B[iB], split)
    
    while True:
        if iA < len(CH_A)-1 and intersection(CH_A[iA+1], CH_B[iB], split) > intersect:
            intersect = intersection(CH_A[iA+1], CH_B[iB], split)
            iA += 1
            continue
        if iB < len(CH_B)-1 and intersection(CH_A[iA], CH_B[iB+1], split) > intersect:
            intersect = intersection(CH_A[iA], CH_B[iB+1], split)
            iB += 1
            continue
        break
    upper = [CH_A[iA], CH_B[iB]]
    
    CH_A = [CH_A[0]] + CH_A[-1:0:-1]
    CH_B = [CH_B[0]] + CH_B[-1:0:-1]
    iA = 0
    iB = 0 
    intersect = intersection(CH_A[iA], CH_B[iB], split)
    
    while True:
        if iA < len(CH_A)-1 and intersection(CH_A[iA+1], CH_B[iB], split) < intersect:
            intersect = intersection(CH_A[iA+1], CH_B[iB], split)
            iA += 1
            continue
        if iB < len(CH_B)-1 and intersection(CH_A[iA], CH_B[iB+1], split) < intersect:
            intersect = intersection(CH_A[iA], CH_B[iB+1], split)
            iB += 1
            continue
        break
    lower = [CH_B[iB], CH_A[iA]]
    
    CH += upper
    CH_B = arrange_CW(CH_B)
    if upper[1] == lower[0]:
        pass
    else:
        temp = (CH_B.index(upper[1]) + 1) % len(CH_B)
        while CH_B[temp] != lower[0]:
            CH += [CH_B[temp]]
            temp = (temp + 1) % len(CH_B)
        CH += [lower[0]]
    if lower[1] == upper[0]:
        pass
    else:
        CH += [lower[1]]
        temp = (CH_A.index(lower[1]) + 1) % len(CH_A)
        while CH_A[temp] != upper[0]:
            CH += [CH_A[temp]]
            temp = (temp + 1) % len(CH_A)
    
    return CH
    

def find_CH(points):
    points = arrange_CW(points)
    l = len(points)
    if l == 0 or l == 1:
        return []
    elif l == 2:
        return [points[0], points[1]]
    elif l == 3:
        return [points[0], points[1], points[2]]
    else:
        split = find_split(points)
        print(split)
        splitA, splitB = split_points(points, split)
        CH_A = find_CH(splitA)
#        CH_A = arrange_CW(CH_A)
#        print("CH_A", CH_A)
        CH_B = find_CH(splitB)
#        CH_B = arrange_CW(CH_B)
#        print("CH_B", CH_B)
        CH = merge(CH_A, CH_B, split)
        return CH
    
    
    
    
    
points = gen_points(200)
#points= [(-3.7077393770700127, 64.28912358641469), (-1.588802434219943, 61.55060249250167), (-3.141972750641145, 92.9726320321032), (10.533064146288496, -64.04925530022057), (10.533064146288496, -64.04925530022057)]
index, value = max(enumerate(points), key=lambda x: x[1][1])
print(points)
xs = [point[0] for point in points]
ys = [point[1] for point in points]
plt.scatter(xs, ys)
print("++++++++++++++++++++++++++++++++++")
CH = find_CH(points)
CH_xs = [point[0] for point in CH]
CH_ys = [point[1] for point in CH]
plt.scatter(CH_xs, CH_ys, marker='X', color='Red')
plt.show()
#print(CH)

#plt.plot[CH_xs, CH_ys]
#a=[(-92.7053099685556, 99.19397567537814), (-47.96154250095617, 90.31146404829889), (1.2435216574613719, 71.14696036717535), (17.06886425654774, -2.309586303909157), (-42.262320898619166, -60.49983811385018), (-79.50298705951684, -84.84019540738853)]
#b= [(31.529575509294204, 53.33785390848453), (44.48439854434764, 72.6605158385911), (53.16348365273083, 78.61229335834537), (83.36718610554718, 36.70511063493976), (52.726277084506336, -71.93633651724303), (32.42375272314467, -23.681631949547224)]
#merge(,24.299219882920973)