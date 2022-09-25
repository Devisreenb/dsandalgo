class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=height[0]
        rightmax =height[len(height)-1]
        l = 0
        r= len(height)-1
        res=0
        while l<r:
            if leftmax<rightmax :
                l+=1
                leftmax = max(leftmax,height[l])
                res += leftmax-height[l]
            else:
                r-=1
                rightmax = max(rightmax,height[r])
                res+=rightmax-height[r]
        return res
                


def trapped(arr):
    water = 0
    j=0
    for i in range(0,len(arr)):
        j = i
        leftmax =0
        rightmax =0
        while(j>=0):
            leftmax = max(leftmax,arr[j])
            j-=1
        j= i
        while(j<len(arr)):
            rightmax=max(rightmax,arr[j])
            j+=1
        water +=min(leftmax,rightmax)-arr[i]
    return water


arr = [4,2,0,3,2,5]
print(trapped(arr))