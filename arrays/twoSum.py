def twosum(arr,k):
    n = len(arr)
    d = {}
    for i,ele in enumerate(arr):
        if k-ele in d:
            return [i,d[k-ele]]
        else:
            d[ele]=i
        
        
arr = [2,4,1,0,9,5]
print(twosum(arr,10))