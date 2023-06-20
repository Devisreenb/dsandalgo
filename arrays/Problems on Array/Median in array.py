class Solution:
    def medianArray(self,arr):
        arr.sort()
        print(arr)
        n = len(arr)
        if n%2 == 1 :
            print(arr[n//2])
        else:
            print((arr[n//2]+arr[n//2-1] )/2)

output = Solution()
output.medianArray([5,6,7,1,2,0,8,9,9,11,12,13])


'''
This is the solution where we sort the array and find median of the array . 
Time complexity : O(NlogN)
'''