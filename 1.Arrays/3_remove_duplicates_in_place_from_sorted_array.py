"""

Brute Force

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = sorted(set(nums))  # returns list
        index =0
        for i in range(0,len(a)):
            nums[i] = a[i]
            index+=1
        
        return index
    
if __name__=="__main__":
    nums = [1,2,2,2,3,3]
    sol = Solution()
    result = sol.removeDuplicates(nums)
    print(f"Unique Elements are: {result}")

"""
# Good Solution

class Solution:
    def removeDuplicates(self,nums:list[int])->int:
         index =0
         for j in range(1,len(nums)):
            if nums[index]!=nums[j]:
               index+=1
               nums[index]=nums[j]
        
         return index+1
              


if __name__=="__main__":
    nums = [1,2,2,2,3,3]
    sol = Solution()
    result = sol.removeDuplicates(nums)
    print(f"Unique Elements are: {result}")