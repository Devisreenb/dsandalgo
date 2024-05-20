'''
class Solution :
    def removeDuplicates(self,arr):
        mark = [True for i in range(len(arr))]
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if arr[i]==arr[j]:
                    mark[j]=False
        for i in range(len(arr)):
            if mark[i]==True:
                print(arr)

output = Solution()
output.removeDuplicates([4,1,3,6,0,9,4,8,5,2,1,1,3])
'''
                
