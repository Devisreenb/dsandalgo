class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}# take an empty dictionary
        for i in nums:
            if i not in d:
                d[i]=1# if element is not in d intialize its count as 1 by inserting it
            else:
                d[i]+=1# if element is present then increment its count (duplicate )
            
        for j in d.values():
            if j>1:
                return True
        return False    

# Time complexity : 