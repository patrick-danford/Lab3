# Move Zeros

"""
Patrick Danford 
Lab 3, Move Zeros

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, 
nums should be [1, 3, 12, 0, 0].

Note: You must do this in-place without making a copy of the array. 
Minimize the total number of operations.
 
"""

nums = [0,10,0,3,4,0,5,0,6]
for num in nums:
    if num == 0:
        nums.pop(nums.index(num))
        nums.append(num)
print nums

