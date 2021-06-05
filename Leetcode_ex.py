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

# 9. Palindrome Number
def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s = str(x)
        print(int(len(s)/2))
        for i in range(0, int(len(s)/2)):
            if(s[i]!=s[-1-i]):
                print(i, -1-i)
                return False
        return True
