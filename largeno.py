def largenomoretime(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    print(f'{arr1[len(arr1)-1]} is the smallest value in arr1')
    print(f'{arr2[len(arr2)-1]} is the smallest value in arr2')


def largenolesstime(arr):
    
    max=arr[0]
    for i in range(0,len(arr)):
        if arr[i] > max :
            max=arr[i]
    return max

if __name__=='__main__':
     arr1 = [2, 5, 1, 3, 0]
     arr2 = [8, 10, 5, 7, 9]
     largenomoretime(arr1,arr2)
     max_arr1=largenolesstime(arr1)
     max_arr2=largenolesstime(arr2)
     
     print(f'The smallest value in arr1 using smallnolesstime: {max_arr1}')
     print(f'The smallest value in arr1 using smallnolesstime: {max_arr2}')
    