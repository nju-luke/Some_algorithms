from numpy import *    

'''
动态规划两个例子
1. 资源分配问题（统筹）
2. 01背包问题

'''

## 资源分配问题
def max_index(A,row_max,k):             #递归找出不同分配组合
    res = []
    if k == 1:
        res.append(row_max)
        return row_max
    temp = list(A[row_max,:,k])
    max_t = amax(temp)
    count_max = temp.count(max_t)
    for i in range(count_max):        
        col_max = temp.index(max_t,i+1)
        ind = max_index(A,row_max-col_max,k-1)
        res.extend((col_max,ind))     
    return res

#value = array([[0,3,5,6,7,6,5],[0,4,6,7,8,9,10],[0,2,5,9,8,8,7],[0,2,4,6,9,8,7]])
#num_fact = 4

value = array([[0,3,5,6,7,6,5],[0,4,6,7,8,9,10],[0,2,5,9,8,8,7]])
num_fact = 3

num_dev = 6
profit = zeros((num_dev+1,num_dev+1,num_fact+1))

for k in range(1,num_fact+1):
    profit_ex = amax(profit[:,:,k-1],1)
    for i in range(num_dev+1):
        for j in range(i+1):
            profit[i,j,k] = value[num_fact-k,j] + profit_ex[i-j]
            
print amax(profit[:,:,-1])

index_dis = max_index(profit,num_dev,num_fact)
print index_dis



# 01 背包问题
n = 5                               #Initialize the data
Weight = array([2,2,6,5,4])
Value = array([6,3,5,4,6])

toltal_w = 10

bag_value = zeros((n,toltal_w+1))           #Initialize the Value function
bag_value[n-1,Weight[n-1]:] = Value[n-1]    # The last line is determined by the last weight and value

for i in range(n-2,-1,-1):                  # Calculate the value of different polices with recursive
    for j in range(toltal_w+1):
        if j < Weight[i]:
            bag_value[i,j] = bag_value[i+1,j]
        else:
            bag_value[i,j] = max(bag_value[i+1,j],
                            bag_value[i+1,j-Weight[i]]+Value[i])

value_list = map(list,bag_value)            # Findout the best police from the value matrix
v_max = amax(value_list)
prio = []
for i in range(n-1):
    if v_max in value_list[i] and v_max not in value_list[i+1]:
        prio.append(i)
        v_max -= Value[i]
if v_max != 0:
    prio.append(i+1)

print amax(bag_value)
print prio

raw_input()
