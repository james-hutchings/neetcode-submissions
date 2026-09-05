class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Can use binary search, similar to minimum of rotated array.
        # REMEMBER: ONE SIDE IS ALWAYS ORDERED.  

        l = 0
        r = len(nums) - 1

        while l <= r:
            
            # Calc m.
            m = l + (r - l) // 2

            # Case where we have found target.
            if nums[m] == target:
                return m

            # Case where left half is sorted.
            if (nums[l] <= nums[m]):
                if (nums[l] <= target < nums[m]):
                    r = m

                else:
                        l = m + 1

            # Case where right half is sorted.
            else:
                if (nums[m] < target <= nums[r]):
                    l = m + 1
                    
                else:
                    r = m

        return -1
