class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        diff=sum(a)-sum(b)
        if diff%2==1:
            return -1
        diff=diff//2
        a.sort()
        b.sort()
        s,e=0,0
        while s<n and e<m:
            curr=a[s]-b[e]
            if curr==diff:
                return 1
            elif curr>diff:
                e+=1
            else:
                s+=1
        return -1
        
        


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends