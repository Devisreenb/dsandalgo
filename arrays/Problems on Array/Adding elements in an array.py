class Solution:
    def insertBeginning(self,arr,k):
        arr.append(0)
        for i in range(len(arr)-2,-1,-1):
            arr[i+1]=arr[i]
        arr[0]=k
        print(arr)
    def insertEnding(self,arr,k):
        arr.append(k)
        print(arr)
    def insertAtPos(self,arr,k,pos):
        arr.append(0)
        for i in range(len(arr)-2,pos-1,-1):
            arr[i+1]=arr[i]
        arr[pos-1]=k
        print(arr)

output = Solution()
arr=[1,2,3,4,5,6,7,8]
output.insertBeginning(arr,1)
output.insertEnding(arr,9)
output.insertAtPos(arr,60,3)


'''
The complexity for insertBeginning : O(N) , insertEnding:O(1) , insertAtPos:O(N)
'''