class Solution :
     def removeDuplicates(self,arr):
          '''
          newarr = list(set(arr))
          print(newarr)

          '''
          i = 0
          for j in range(1,len(arr)) :
               if arr[i] != arr[j] :
                     i = i+1  
                     arr[i] = arr[j]
                     
          print(arr[0:i+1])
                        
        
output = Solution()
output.removeDuplicates([2,2,4,5,6,6,7,7,7,8])

'''
The bruteforce approach involves converting list into set and then to list .
Time complexity : O(N)
Space complexity:O(N)

The optimal solution involves two pointer approach ,where two pointers are used , one pointer moves with checking 
if elements are different if so then replaces the element in first pointer with element in second and increments first pointer value
Time complexity:O(N)
'''