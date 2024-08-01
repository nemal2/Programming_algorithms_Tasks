
# game_of_level

def maxLevel(h:int,m:int) -> int:
    # code here
    dp = [[0 for j in range(1500)] for i in range(1500)]
    def rec(h,m):
        if h<=0 or m<=0:
            return 0
        if dp[h][m] != 0:
            return dp[h][m]
        a = rec(h-5+3,m-10+2)+2
        b = rec(h-20+3,m+5+2)+2
        dp[h][m] = max(a,b)
        return dp[h][m]
    return rec(h,m)-1

ans = maxLevel(20,20)
print(ans)