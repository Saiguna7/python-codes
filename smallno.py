def smallnomoretime(arr1, arr2):
    arr1.sort()
    arr2.sort()
    print(f'{arr1[0]} is the smallest value in arr1')
    print(f'{arr2[0]} is the smallest value in arr2')

def smallnolesstime(arr):
    if not arr:  # Check if the array is empty
        return None
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
    return min_value

if __name__ == '__main__':
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    
    smallnomoretime(arr1, arr2)
    
    min_arr1 = smallnolesstime(arr1)
    min_arr2 = smallnolesstime(arr2)
    
    print(f'The smallest value in arr1 using smallnolesstime: {min_arr1}')
    print(f'The smallest value in arr2 using smallnolesstime: {min_arr2}')