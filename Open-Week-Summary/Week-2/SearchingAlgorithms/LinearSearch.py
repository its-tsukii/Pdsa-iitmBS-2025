def naiveSearch(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return False
        
print(naiveSearch([1,2,3,7,5,4,3],6))
print(naiveSearch([1,2,3,7,5,4,3],3))