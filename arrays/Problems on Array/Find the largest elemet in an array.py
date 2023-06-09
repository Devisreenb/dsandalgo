class Solution:
    def largestElement(self,arr):
        max = arr[0]
        n = len(arr)
        for i in range(0,n):
            if (arr[i]>max):
                max = arr[i]
        return max

output = Solution()
print(output.largestElement([9,0,12,3,4,7,2]))

"""
This approach is the optimal solution which uses a variable max and finds the largest element by looping through the array once .
Time complexity : O(N)

BruteForce : 
Here we can sort the array and return the arr[n-1] element . 
Time complexity : O(NlogN)
"""