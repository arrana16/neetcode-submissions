from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = {}
        longest = 0
        for n in nums:
            if n not in numMap:
                total = 1
                if n-1 in numMap and n+1 in numMap:
                    total += numMap[n-1] + numMap[n+1]
                    numMap[n-numMap[n-1]] = total
                    numMap[n+numMap[n+1]] = total
                    numMap[n] = total
                elif n-1 in numMap:
                    total += numMap[n-1]
                    numMap[n] = total
                    numMap[n-numMap[n-1]] = total
                elif n+1 in numMap:
                    total += numMap[n+1]
                    numMap[n] = total
                    numMap[n+numMap[n+1]] = total
                else:
                    numMap[n] = 1
                
                longest = max(total, longest)
                
        return longest