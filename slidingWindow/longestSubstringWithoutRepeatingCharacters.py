def lssnor(arr):
    new = list(arr)
    maxi =0 
    for i in range(len(arr)):
        for j in range(i,len(arr)):
           if len(arr[i:j+1])==len(set(arr[i:j+1])):
               maxi = max(len(arr[i:j+1]),maxi)
    return maxi

inp = "pwwkew"
print(lssnor(inp))