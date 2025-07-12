"""
Reverse List In-Place

Description:

Given an integer array nums, reverse the elements of the array in-place and return it.
You must do this without using any extra list.

Example:

Input: nums = [1,2,3,4,5]
Output: [5,4,3,2,1]

Constraints:

1 <= len(nums) <= 10^4
-10^4 <= nums[i] <= 10^4

"""
    
def reverse_list_inplace_manual(my_list):
    left = 0
    right = len(my_list) - 1
    while left < right:
        my_list[left], my_list[right] = my_list[right], my_list[left] # Swap elements
        left += 1
        right -= 1
    return my_list

nums = [1, 2, 3, 4, 5]
print(f"Original list: {nums}")
reversed_nums = reverse_list_inplace_manual(nums)
print(f"Reversed list (in-place): {reversed_nums}")
print(f"Original list after reversal: {nums}") # Verify it's modified in-place