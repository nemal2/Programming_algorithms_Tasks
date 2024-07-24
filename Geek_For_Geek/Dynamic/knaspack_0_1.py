class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
        
        def knapSackRecursive(W, wt, val, n):
            # Base case: no items left or no remaining capacity
            if n == 0 or W == 0:
                return 0
            
            # If the value is already computed, return it
            if dp[n][W] != -1:
                return dp[n][W]
            
            # If weight of the nth item is more than the capacity W, it cannot be included
            if wt[n - 1] > W:
                dp[n][W] = knapSackRecursive(W, wt, val, n - 1)
            else:
                # Return the maximum of two cases:
                # (1) nth item included
                # (2) not included
                dp[n][W] = max(
                    val[n - 1] + knapSackRecursive(W - wt[n - 1], wt, val, n - 1),
                    knapSackRecursive(W, wt, val, n - 1)
                )
            
            return dp[n][W]
        
        return knapSackRecursive(W, wt, val, n)


