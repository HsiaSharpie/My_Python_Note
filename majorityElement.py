class Solution:
    def majorityElement(self, nums):
        ele_count = {}
        for index, num in enumerate(nums):
            if num not in ele_count:
                ele_count[nums[index]] = 1
            else:
                ele_count[num] += 1

        return max(ele_count, key=ele_count.get)

given_nums = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6]


if __name__ == "__main__":
    print(Solution().majorityElement(given_nums))
