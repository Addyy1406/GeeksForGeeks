#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
     
        count=0 
        for i in range(1,r*2):  
            for j in range(1,r*2):
                diagonal = ((i*i) + (j*j))**0.5
                if(diagonal <= r*2):
                    count+=1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends