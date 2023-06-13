class Solution :
    def reverseArray(self,arr):
        '''
        Recursion approach 
        n = len(arr)
        for i in range(0,n//2):
            arr[n-i-1],arr[i] = arr[i],arr[n-i-1]
        return arr
       '''
        n= len(arr)
        p1 = 0
        p2 = n-1
        while p1<p2:
            arr[p1],arr[p2] = arr[p2],arr[p1]
            p1=p1+1
            p2=p2-1
        return arr
    
output = Solution()
print(output.reverseArray([0,9,8,6,3]))

'''
This is optimal solution which uses two pointer approach , we use two pointer and keep swaping the first and last elements .
The other optimal solution is a recursion approach , we swap first and last elements by traversing through the array by half.
Time complexity : O(N)

Bruteforce :
This approach requires taking a new array and placing the elements in reverse order 
Time complexity : O(N)
Space complexity : O(N)

'''
        

        