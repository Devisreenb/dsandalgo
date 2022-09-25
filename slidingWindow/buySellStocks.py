class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi =0
        mini=prices[0]
        for i in range(len(prices)):
            mini = min(prices[i],mini)
            maxi = max(prices[i]-mini,maxi)
        return maxi
        
        
def sell(arr):
    maxi =0 
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            maxi = max(arr[j]-arr[i],maxi)
    return maxi

inp = [7,1,5,3,6,4]
print(sell(inp))