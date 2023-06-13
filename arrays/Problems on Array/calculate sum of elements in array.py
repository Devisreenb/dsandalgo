class Solution:
    def sumofElements(self,arr):
        #built in function
        x = sum(arr)
        print(x)
        # loop through the array
        n = len(arr)
        summ = 0 
        for i in range(n):
            summ += arr[i]
        print(summ)


output = Solution()
output.sumofElements([9,6,5,1,2,9])

'''
The sum of elements of an array can be calculated by summing up all elements of the array of by just using direct built-in function sum()
Time complexity : O(N)
'''