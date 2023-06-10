import sys
class Solution :
    def SecondSmallestLargest(self,arr):
        n = len(arr)
        secondmin = min = sys.maxsize
        secondmax = max = -sys.maxsize-1
        for i in range(0,n):
            if arr[i]<min:
                min = arr[i]
            if arr[i]>max:
                max = arr[i]
        for i in range(0,n):
            if arr[i]<secondmin and arr[i]!=min  :
                secondmin = arr[i]
            if arr[i]>secondmax and arr[i]!=max:
                secondmax = arr[i]
        return (secondmin,secondmax)

output = Solution()
print(output.SecondSmallestLargest([0,2,3,5,4,5]))

'''
This is optimal solution which uses for loops and finds the min and max elements intially and later looping through again finding the second smallest
and largest element by finding minimum element which is not equal to min element and finding maximum element not equal to max element.
Time complexity : O(N)

Bruteforce :
This approach is most suitable when no duplicates exist in the list. Here we sort the list and find arr[1],arr[n-1] elements .
Time Complexity : O(NlogN)
'''


        