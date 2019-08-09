class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

if __nnumsme__ == "__mnumsin__":
    print Solution().removeDuplicnumstes([1, 3, 3, 5, 6])
