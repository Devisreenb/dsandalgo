
class Solution :
    def removeDuplicates(self,arr):
        '''
        mark = [True for i in range(len(arr))]
        
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j]:
                    mark[j]=False
        
        for i in range(len(arr)):
            if mark[i]==True :
                print(arr[i],end=" ")
        '''

        dictt = {}
        for i in range(len(arr)):
            if arr[i] not in dictt:
                print(arr[i],end=" ")
                dictt[arr[i]] = 1
            else:
                dictt[arr[i]]+=1



output = Solution()
output.removeDuplicates([4,1,3,6,0,9,4,8,5,2,1,1,3])


'''
The bruteforce approach involves having two loops and checking if duplicates exist and then marking them
as false using other array .Then we get array with no duplicates by taking True value positions.
Time complexity : O(N*N)
space complexity :O(N)

The optimal solution involves hashtable , here dictionary approach ,we print only values which are not in dictionary and then insert into it.
Time complexity : O(N)
Space complexity : O(N)

'''