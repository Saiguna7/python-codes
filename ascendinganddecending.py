if __name__=='__main__':
     arr= [8,7,1,6,5,9];
     n=len(arr)
     arr.sort()
     for i in range(0,int(n/2)):
         print(arr[i],end=" ")
     for i in range(n-1,int(n/2) -1,-1):
         print(arr[i],end=" ")