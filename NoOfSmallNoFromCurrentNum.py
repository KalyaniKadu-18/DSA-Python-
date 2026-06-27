from typing import List

def SmallNoFromCurrent(nums: List[int]) -> List[int]:
    ans = []
    
    for i in nums:
        c = 0
        for j in nums:
            if j < i:
                c += 1
        ans.append(c)
    
    return ans

nums = [3,4,5,6,2,8]
print(SmallNoFromCurrent(nums))