""" 

Brute Force

class Solution:
    def secondLargestElement(self,nums):
        size = len(nums)
        if size<2:
            return -1
        nums.sort()
        largest = nums[-1]
        second_largest =-1
        for i in range(size-2,-1,-1):
            if nums[i]!=largest:
                second_largest=nums[i]
                break
        return second_largest


if __name__=="__main__":
    nums = [1, 2, 4, 6, 7, 5]
    sol = Solution()
    result = sol.secondLargestElement(nums)
    print(f"Second Largest Element: {result}")


 """

"""


 Better Solution
 
class Solution:
    def secondLargestElement(self,nums):
         size = len(nums)
         largest = nums[0]
         for i in range(0,size):
            if nums[i]>largest:
                largest = nums[i]
         
         second_largest = -1
         for i in range(0,size):
             if nums[i]!=largest and nums[i]>second_largest:
                 second_largest = nums[i]
         
         return second_largest



if __name__=="__main__":
    nums = [1, 2, 4, 6, 7, 5]
    sol = Solution()
    result = sol.secondLargestElement(nums)
    print(f"Second Largest Element: {result}")
 
 """

# Optimal Solution

# if someone becomes largest then previous largest will become second largest and if number is lesser than largest then only compare it with second largest

class Solution:
    def secondLargestElement(self, nums):
        size = len(nums)
        if size<2:
            return -1
        
        largest = nums[0]
        second_largest = float('-inf')

        for i in range(0,size):
            if nums[i]>largest:
                second_largest=largest
                largest = nums[i]
            elif nums[i]!=largest and nums[i]>second_largest:
                second_largest = nums[i]

        return second_largest if second_largest!=float('-inf') else -1



if __name__=="__main__":
    nums = [1, 2, 4, 6, 7, 7, 5]
    sol = Solution()
    result = sol.secondLargestElement(nums)
    print(f"Second Largest Element: {result}")


"""

Always Remember: 

- In Python , set is iterable but not indexable 
- Python does not support incremental Operator
- Set is in random operator
- sorted() returns list , no matter whatever you pass

- time complexity of sorted(set(nums)) is O(n) + O(nlogn)

"""