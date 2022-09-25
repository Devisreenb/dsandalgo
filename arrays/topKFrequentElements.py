import heapq
def topk(arr,k):
    ans =[]
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    for key,val in d.items():
        if len(ans)<k:
            heapq.heappush(ans,[val,key])
        else:
            heapq.heappushpop(ans,[val,key])
    return [key for value,key in ans]
    

arr = [1,1,1,1,1,2,2,2,3,3,3,5,5,5]
k = 3
print(topk(arr,k))  

"""

Time complexity for hashing is O(n)
build heap takes O(k) coz bilding k size heap
then slide ffrom rest all (N-k) elements .Use push & pop
O((N-k)logk)

time complexity " O(N+k+n-k log k) = O(N+Nlogk)
"""

"""
step1: hashing O(n)
step2 : build heap O(n)
step 3 :extract max k times O(klogn)

time complexity = O(n+n+klogn)
"""

""" what is heapq?
it is a datastructure that each parent node is less than or equal to
its child node .In python it is implemented using the heapq module .
"""