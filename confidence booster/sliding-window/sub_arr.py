"""
Subarray Sum Equals Target (Brute Force)
Given an integer array nums and an integer target, return True if there exists a contiguous subarray whose sum equals target, else return False.


Input: nums = [1,2,3,7,5], target = 12
Output: True
Explanation: Subarray [2,3,7] sums to 12

Constraints:

1 <= len(nums) <= 10^3 (small because brute force is fine here)
-10^4 <= nums[i], target <= 10^4

    
"""
def has_subarray_with_sum(nums, target):
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == target:
                return True
    return False


nums = [1,2,3,7,5]
target = 12
print(has_subarray_with_sum(nums=nums, target=target))