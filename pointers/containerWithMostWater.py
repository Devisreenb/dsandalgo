class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxi =0
        while i<=j:
            maxi = max(min(height[i],height[j])*(j-i),maxi)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxi
        """
        maxi =0
        for i,el1 in enumerate(height):
            for j,el2 in enumerate(height):
                wc= min(el1,el2)*(j-i)
            maxi =max(maxi,wc)
        return maxi
        """