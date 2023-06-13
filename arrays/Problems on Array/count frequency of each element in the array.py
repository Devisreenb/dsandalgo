class Solution : 
    def countFreq(self,arr):
        '''
        # BruteForce approach 

        n = len(arr)
        visited = [0 for i in range(n)]
        for i in range(n):
            count = 1
            if visited[i]==-1:
                continue
            for j in range(i+1,n):
                if arr[i]==arr[j]:
                    visited[j]=-1
                    count = count+1
            print(arr[i]," ", count)

            '''
        n = len(arr)
        dictt = {}
        for i in range(n):
            if arr[i] not in dictt :
                dictt[arr[i]] = 1 
            else :
                dictt[arr[i]] +=1 
        print(dictt)
        for item,val in dictt.items():
            print(item,val)
            

output = Solution()
output.countFreq([2,3,4,2,3,1,6,6,8])

'''
The brute force approach it takes space : O(N) as it uses visited array and it takes two loops approach and prints the count of different elements.
Time complexity : O(N*N)

The optimal approach is mapping method, we can use dictionaries and store each value count and print them 
Time complexity : O(N)
'''


                
