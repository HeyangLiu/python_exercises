from typing import List


def check(s):
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for c in s:
        if(c in vowel):
            count+=1
    return count

print(check("hourly new day"))

# 1.Two Sum
def twoSum(nums: List[int], target: int):
    l = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j]==target):
                l=[i,j]
                break
    return l


