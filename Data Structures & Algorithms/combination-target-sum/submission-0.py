class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def search(start, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            elif start >= len(nums) or total > target:
                return
            
            curr.append(nums[start])
            search(start, curr, total + nums[start])
            curr.pop()
            search(start+1, curr, total)

        search(0, [], 0)
        return res

