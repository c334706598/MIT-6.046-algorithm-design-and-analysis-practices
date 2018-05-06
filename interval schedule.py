import random


class interval:
    def __init__(self, start, finish, weight=1):
        if start < finish:
            self.start = start
            self.finish = finish
            self.length = self.finish - self.start 
            self.weight = weight
        else:
            self.start = None
            self.finish = None
            self.length = 0 
            self.weight = 0
    def show(self):
        print('start=', self.start, "  ", "finish=", self.finish, "  ",
              "weight=", self.weight)
    
def gen_intervals(start, finish, num, var_weight=False):
    res = []
    for i in range(num):
        temp1 = random.uniform(start, finish)
        temp2 = random.uniform(temp1, finish)
        res.append(interval(temp1, temp2))
    res.sort(key=lambda x: x.finish, reverse=False)
    if var_weight == True:
        for i in range(len(res)):
            res[i].weight = random.uniform(1, 10)
    return res

def dropIncompatible(intervals, interval):
    res = []
    for i in intervals:
        if i.finish < interval.start or i.start > interval.finish:
            res.append(i)
    return res

def find_later_intervals(intervals, interval):
    res = []
    for i in intervals:
        if i.start > interval.finish:
            res.append(i)
    return res

def find_max_num_intervals(intervals):
    for i in intervals:
        i.show()
    
    while any(intervals):
        temp = intervals[0]
        res.append(temp)
        intervals = dropIncompatible(intervals, temp) 

    print("====================================")
    for i in res:
        i.show()
    print("max num of intervals is ", len(res))
    
def find_max_weight_intervals(intervals):
    intervals.sort(key=lambda x: x.start, reverse=False)
    for i in intervals:
        i.show()
        
    l = len(intervals)
    dp = [0 for _ in range(l)]
    for k in range(l):
        i = intervals[~k]
        temp = find_later_intervals(intervals, i)
        if len(temp) == 0:
            dp[~k] = [i,], i.weight
        else:
            dp[~k] = dp[~(len(temp)-1)][0]+[i], dp[~(len(temp)-1)][1]+i.weight

#    print(dp)   
    max_weight = 0
    max_index = 0    
    for i in range(len(dp)):
        if dp[i][1] > max_weight:
            max_weight = dp[i][1]
            max_index = i
    print("====================================")
    for i in dp[max_index][0][::-1]:
        i.show()
        
    print("max weight = ", dp[max_index][1])
    return dp[max_index]
        
    
    

### Test: interval schedule without weights: greedy algorithm of earliest finish time
#res = []
#min_time = 0
#max_time = 100
#num_interval = 100
#intervals = gen_intervals(min_time, max_time, num_interval, var_weight=True)
#find_max_num_intervals(intervals)

### Test: interval schedule with weights: dp algorithm for largest total weights
res = []
min_time = 0
max_time = 100
num_interval = 10
intervals = gen_intervals(min_time, max_time, num_interval, var_weight=True)
find_max_weight_intervals(intervals)

   
