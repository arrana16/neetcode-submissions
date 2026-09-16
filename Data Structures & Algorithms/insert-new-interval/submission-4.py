class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_index = ()
        end_index = ()

        if (len(intervals) == 0):
            return [newInterval]

        l = 0
        r = len(intervals) - 1
        middle = -1
        while l <= r:
            middle = (l + r) // 2
            print(middle)
            interval = intervals[middle]
            if interval[0] <= newInterval[0] <= interval[1]:
                start_index = (middle, "inside")
                break
            elif newInterval[0] < interval[0]:
                start_index = (middle, "before")
                r = middle - 1
            elif newInterval[1] > interval[1]:
                start_index = (middle + 1, "before")
                l = middle + 1
        
        print(start_index)

        # find end_index
        l = 0
        r = len(intervals) - 1
        middle = -1
        while l <= r:
            middle = (l + r) // 2
            print(middle)
            interval = intervals[middle]
            if interval[0] <= newInterval[1] <= interval[1]:
                end_index = (middle, "inside")
                break
            elif newInterval[1] > interval[1]:
                end_index = (middle, "after")
                l = middle + 1
            elif newInterval[1] < interval[0]:
                end_index = (middle - 1, "after")
                r = middle - 1
        
        print(end_index)

        res = []
        if (end_index[0] == -1):
            res.append(newInterval)
            for interval in intervals:
                res.append(interval)
            return res
        elif start_index[0] == len(intervals):
            for interval in intervals:
                res.append(interval)
            res.append(newInterval)
            return res
        elif start_index[0] > end_index[0]:
            res = [0] * (len(intervals)+1)
            new_flag = False
            res[start_index[0]] = newInterval
            for i in range(len(intervals)):
                if (i >= start_index[0]):
                    res[i + 1] = intervals[i]
                else:
                    res[i] = intervals[i]
            return res
        else:
            res = []
            added = False
            for i in range(len(intervals)):
                if start_index[0] <= i <= end_index[0]:
                    if not added:
                        res.append([min(newInterval[0], intervals[start_index[0]][0]), max(newInterval[1], intervals[end_index[0]][1])])
                        added = True
                else:
                    res.append(intervals[i])
            return res

