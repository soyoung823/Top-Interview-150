"""
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
def majorityElement(nums):
    
    n = len(nums)
    counter = Counter(nums)
    for num, count in counter.items():
        # if majority
        if n % 2 == 0 # even
            if count >= n // 2: # majority
                return num
        else: # odd
            if count >= n // 2 + 1: # majority when odd
                return num

# TC: O(n), SC: O(n)


# follow up with SC O(1)?
def majorityElement(nums):
    count = 0
    candidate = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1

        else: # diff
            count -= 1
    return candidate

# TC: O(n), SC: O(1)
