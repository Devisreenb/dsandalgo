class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl= list(s)
        sl.sort()
        tl =list(t)
        tl.sort()
        if(sl==tl):
            return True
        else:
            return False
        

"""

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

"""

#  Time complexity : O(n)   [ string to list conversion]
