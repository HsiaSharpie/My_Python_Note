class Solution:
    def TwoSum(self, nums, target):
        value_2_index = {}
        for index, num in enumerate(nums):
            if target - num in value_2_index:
                return [value_2_index[target - num], index]
            else:
                value_2_index[num] = index


given_nums = [2, 7, 11, 15]
target = 9

if __name__ == "__main__":
    print(Solution().TwoSum(given_nums, target)
