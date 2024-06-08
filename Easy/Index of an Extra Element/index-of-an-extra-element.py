class Solution:
    def findExtra(self,n,a,b):
        a.sort();
        b.sort();
        c=-1
        b.extend(a)
            
        for i in a:
            c+=1
            if i !=b[c]:
                break
            
        return c


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends