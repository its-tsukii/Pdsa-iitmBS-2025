def InsertionSort(nums):
    n = len(nums)
    if n < 1:
        return nums
    for i in range(n):
        j = i
        while( j > 0 and nums[j] < nums[j-1]):
            nums[j],nums[j-1] = nums[j-1],nums[j]
            j = j - 1
    return nums 

print(InsertionSort([4,6,8,2,1,4,9,8]))