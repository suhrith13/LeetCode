take a array and designate left pointer and right pointer ( indexes -> 0 and n-1)
while the left pointer is smaller than right pointer calculate the mid point 
if mid point is less that or equal to right pointer it means that the min element is either the mid point or on the left side so discard the right side elements, update the right pointer to mid element
if thats not the case move the mid pointer to the right, once you find the min element L == R, then return the element.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
