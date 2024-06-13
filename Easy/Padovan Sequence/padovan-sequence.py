#User function Template for python3
class Solution:
    mod=10**9+7
    def padovanSequence(self, n):
        a,b,c=1,1,1
        for i in range(3,n+1):
            a,b,c=b,c,(a+b)%self.mod
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends