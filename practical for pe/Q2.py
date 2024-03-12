def find_balanced_i(arr):
    right_sum = 0
    left_sum = 0
    
    for i in range(len(arr)):
        left_sum = sum(arr[0:i])
        right_sum = sum(arr[i-1:])
        if left_sum == right_sum:
            return 'YES'
            
    return 'NO'

arr = [2, 3, 1, 6, 1, 2, 3]
print(find_balanced_i(arr))
        
        