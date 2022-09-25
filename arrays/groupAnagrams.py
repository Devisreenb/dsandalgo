def grpanagrams(arr):
    lis = []
    new =[0 for i in arr]
    for i in range(len(arr)):
        temp =[]
        for j in range(i,len(arr)):
            if sorted(arr[i])==sorted(arr[j]) and i!=j and new[j]==0:
                temp.append(arr[j])
                new[j]=-1
        if new[i]!=-1 :
            temp.append(arr[i])
        if len(temp)!=0:
             lis.append(temp)
    return lis


strs = ["eat","tea","tan","ate","nat","bat"]



def ganagrams(arr):
    d ={ }
    for ele in arr:
        current = sorted(ele)
        current ="".join(current)
        if current in d:
            d[current].append(ele)
        else:
            d[current]=[ele]
    ans = []
    for ele in d:
        ans.append(d[ele])
    return ans 


print(ganagrams(strs))