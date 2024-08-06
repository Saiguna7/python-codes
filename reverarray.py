def array(arr,n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
def reversearr(arr,start,end):
    if start <end:
       arr[start],arr[end]=arr[end],arr[start]
       reversearr(arr,start+1,end-1)

if __name__=='__main__':
    arr=[5,4,3,2,1]
    n=len(arr)
    reversearr(arr,0,n-1)
    array(arr,n)