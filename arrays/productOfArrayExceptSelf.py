from asyncio.proactor_events import _ProactorDuplexPipeTransport


class Solution:
    def productExceptSelf(self, nums) :
        prod = 1
        for i in range(len(nums)):
            prod*=nums[i]
        for j in range(len(nums)):
            nums[j]=prod//nums[j]
        return nums


def prode(arr):
    res = [1]*(len(arr))

    prefix = 1
    for i in range(len(arr)):
        res[i]=prefix
        prefix *= arr[i]
    postfix =1 
    for i in range(len(arr)-1,-1,-1):
        res[i]*= postfix 
        postfix *=arr[i]
    return res
arr = [1,2,3,8,4]
print(prode(arr))

        
        