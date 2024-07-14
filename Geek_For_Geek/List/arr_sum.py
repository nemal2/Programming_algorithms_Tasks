class Solution:
    def subArraySum(self, arr, n, s):

        if s==0:
            for i in range(n):
                if arr[i]==0:
                    return i+1,i+1
            return [-1]
        
        for i in range(n):
            for j in range(n):
                if i<=j and sum(arr[i:j])==s:
                    return i+1,j

        for k in range(n):
                if arr[k]==s:
                    return k+1,k+1      
        return [-1]

           

# Example usage
sol = Solution()
print(sol.subArraySum([1, 2, 3, 7, 5], 5, 12))  # Output: (2, 4)
print(sol.subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))  # Output: (1, 5)
print(sol.subArraySum([7, 2, 1], 3, 2))  # Output: (2, 2)
print(sol.subArraySum([5, 3, 4], 3, 2))  # Output: [-1]
print(sol.subArraySum([1, 2, 3, 4], 4, 0))  # Output: [-1]
print(sol.subArraySum([5], 1, 5))  # Output: (1,1)