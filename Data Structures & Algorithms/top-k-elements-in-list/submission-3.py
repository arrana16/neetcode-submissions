class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [None] * len(nums)
        freqMap = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        for item in freqMap.items():
            if freqList[item[1]-1] is None:
                freqList[item[1]-1] = [item[0]]
            else:
                freqList[item[1]-1].append(item[0])


        k_nums = []
        for i in range(len(freqList)):
            a = freqList[len(freqList)-1-i]
            if not a is None:
                for num in a:
                    k_nums.append(num)
            if len(k_nums) >= k:
                return k_nums
        return k_nums
            

        