def lonC(arr):
    s = set(arr)
    longest = 0
    for i in arr:
        if i in s:
            length = 1
        while i+length in s:
            length += 1
        longest = max(length,longest)
    return longest

arr = [100,4,200,1,3,2]
print(lonC(arr))