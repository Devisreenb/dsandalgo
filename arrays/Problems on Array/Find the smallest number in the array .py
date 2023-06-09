class Solution :
    def smallestElement(self,arr):
        n=len(arr)
        min = arr[0]
        for i in range(0,n):
            if (arr[i]<min):
                min = arr[i]
        return min


output= Solution()
print(output.smallestElement([9,6,8,2,3,0,1]))
 
'''
This is best approach of using min variable and finding the smallest element in one loop through the array 
Time complexity : O(N)

Bruteforce approach : 
We can sort the array and return arr[0] element ,the smallest one. arr.sort() and return arr[0]
Time complexity : O(NlogN)
'''