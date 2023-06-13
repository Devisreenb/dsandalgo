class Solution:
    def arrayIncreasingDecreasing(self, arr):
        n = len(arr)
        arr.sort()
        print(*arr[:n//2],*arr[-1:n//2-1:-1],sep= " ")

output = Solution()
output.arrayIncreasingDecreasing([2,3,1,8,9,0,4,5])


'''
This is the solution where we sort and print the first half and then print the reverse of the second half .

Time complexity : O(NlogN)
'''