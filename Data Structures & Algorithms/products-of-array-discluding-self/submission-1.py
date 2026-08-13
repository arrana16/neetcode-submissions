class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        preList = [0] * n
        sufList = [0] * n

        prodList = []

        preList[0] = nums[0]
        sufList[n-1] = nums[n-1]


        for i in range(1, n):
            preList[i] = preList[i-1] * nums[i]

        for i in range(1, n):
            sufList[n-1-i] = sufList[n-i] * nums[n-1-i]

        for i in range(0, n):
            if i == 0:
                prodList.append(sufList[i+1])
            elif i == n - 1:
                prodList.append(preList[i-1])
            else:
                prodList.append(preList[i-1] * sufList[i+1])

        return prodList