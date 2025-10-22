def idk(nums,target):
    none = []
    for i in range(len(nums)):
        for t in range(i+1,len(nums)):
            if nums[i]+nums[t]==target:
                return[i,t]
    return none
print(idk([2,7,11,15],9))
print(idk([3,2,4],6))
print(idk([3,3],6))