#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = []  
n = int(input('Enter the number of elements in list \n'))
print('Enter the elements of the list')

for i in range(0, n):
    ele = int(input())  
    nums.append(ele)
    
target = int(input('Enter the target number \n'))

def two_sum(the_list,target):
    for i in range(len(the_list)):
        for j in range(len(the_list)):
            if ((the_list[i] + the_list[j]) == target) and (i != j):
                return [i,j]

print('the required indexes are:')
print(two_sum(nums, target))
