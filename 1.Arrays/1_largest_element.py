"""

 Brute Force
 
class Solution:
    def largestElement(self,nums):
        nums.sort()
        largest = nums[-1]
        return largest
    

if __name__=="__main__":
    nums = [3, 2, 1, 5, 2]
    sol = Solution()
    result = sol.largestElement(nums)
    print(f"Largest Element: {result}")
 
 
 """

# Optimal Approach

class Solution:
    def largestElement(self, nums):
        size = len(nums)
        largest = nums[0]
        for i in range(0,size):
            if nums[i]>largest:
                largest = nums[i]
        return largest
    
if __name__=="__main__":
    nums = [3, 2, 1, 5, 2]
    sol = Solution()
    result = sol.largestElement(nums)
    print(f"Largest Element: {result}")



