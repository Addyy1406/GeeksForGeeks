#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        # check the last element and check if it is bigger
        # or smaller than the key
        if key not in arr:
            return -1
            
        j = arr.index(key)
        return j
        
        # if key < last element then find the rotation count
        sarr = sorted(arr)
        if arr[-1] >= key:
            # go backwards
            for j in range(N-1, -1, -1):
                if arr[j] == key:
                    return j
                    
        else:
            # modified binary search
            # start at mid and determine if need to expand or contract
            # figure out if it is in first half or second half
            mid = N//2
                
            l = 0
            r = N//2
            ans = -1
            
            while ans == -1:
                mid = (l+r)//2
                if arr[mid] == key:
                    ans = mid
            
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends