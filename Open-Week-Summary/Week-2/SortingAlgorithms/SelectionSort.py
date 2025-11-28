def SelectionSort(nums):
    n = len(nums)
    if n < 1:
        return nums
    for i in range(n):
        minPos = i
        for j in range(i+1, n):
            if(nums[j] < nums[minPos]):
                minPos = j
        nums[i],nums[minPos] = nums[minPos],nums[i]
    return nums

print(SelectionSort([4,6,7,3,5,2,1,8]))