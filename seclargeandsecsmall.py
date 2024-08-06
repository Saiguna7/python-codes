
def seclarge_secsmallmoretime(arr,n):
    
    if n==0 and n==1:
        print(-1,-1)
    arr.sort()
    print(f'{arr[1]} second small number and {arr[n-2]} second large number')    

  

def seclarge_secsmalllesstime(arr,n):
    
    if n==0 and n==1:
        print(-1,-1)
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)
    
    
if __name__=='__main__':
    arr = [1, 2, 4, 6, 7, 5];
    
    n=len(arr)
    
    seclarge_secsmallmoretime(arr,n)
    
    seclarge_secsmalllesstime(arr,n)
    
    