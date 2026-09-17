class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(num):
            count = 0
            while num > 0:
                num &= num-1
                count += 1
            return count
        
        res = []
        for i in range(n+1):
            res.append(count_ones(i))

        return res