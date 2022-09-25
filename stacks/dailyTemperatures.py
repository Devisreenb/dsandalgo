class Solution:
    def dailyTemperatures(self, temperatures) :


        n=len(temperatures)
        stack = []
        ans = [0]*n
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                t=ans[stack.pop()]=i-stack[-1]
                print(t)
            stack.append(i)
        return ans
        """
        new = []
        for i in range(len(temperatures)):
            count =0
            for j in range(i,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    count = j-i
                    break
            new.append(count)
            
        return new
        """


s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
