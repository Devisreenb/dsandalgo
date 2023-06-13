class Solution:
    def avgArray(self,arr):
        total = sum(arr)
        avg = total//len(arr)
        print(avg)


output = Solution()
output.avgArray([6,3,2,5,7,2,1])

'''
The average can be calculated as coded .
Time Complexity : O(N)
'''