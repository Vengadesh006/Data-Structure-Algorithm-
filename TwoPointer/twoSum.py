def twoSum(nums,target) :

    low = 0 

    high = len(nums) - 1 

    while low < high : 

        current = nums[low] + nums[high]

        if target < current :

            high -= 1

        elif target > current : 

            low += 1

        else : 

            return [low , high]
        
    return None

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
