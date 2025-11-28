def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while(left <= right):
        mid = (left + right) // 2
        if(target > mid):
            left = mid + 1
        elif(target < mid):
            right = mid - 1
        else:
            return mid
    return False

print(binarySearch([1,2,3,4,5,6,7,8,9],4))