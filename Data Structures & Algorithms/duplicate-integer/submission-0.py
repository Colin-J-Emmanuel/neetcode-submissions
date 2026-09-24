class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # is the array always going to be sorted?
        # Approach: two pointers (works with sorted array)
        # Case 1: sort the array ourselves
        """
        sort the array
        - use nested for loop and compare elements are both indices. if they
        are equal, then we return True. if not, False
        """
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True

        return False