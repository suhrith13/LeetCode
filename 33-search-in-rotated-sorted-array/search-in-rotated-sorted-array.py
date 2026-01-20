once you initialise and fint the mid point, if the target is the mid point reutrn it. 
Now we need to make sure left half is sorted(it may or may not be sorted). Once it is sorted, if the target is btw left and mid point we search from right to mid -1, if not then we search from left to mid + 1
Now we make sure right half is sorted, then we shorten the search from left to mid + 1 and right to mid - 1.
if the target is not found in any sides we return -1 as per the qs.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2


            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
