class Solution:
    def blockSwap(self,arr,k):
        n = len(arr)
        newarr =[]
        for i in range(k,n):
            newarr.append(arr[i])
        for i in range(0,k):
            newarr.append(arr[i])
        print(newarr)



output = Solution()
output.blockSwap([9,8,3,2,5,1],2)

'''
The brute force approach involves new arr and placing the two parts of array into it .
Time Complexity : O(N)
space complexity : O(N)

The optimal solution involves swapping the elements in the array 
Time complexity : O(N)
'''


