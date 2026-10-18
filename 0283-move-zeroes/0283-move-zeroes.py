class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=nums.count(0)

        for i in range(len(nums)):
            try:
                found = nums.index(0)
                nums.pop(found)
            except ValueError:
                continue
        
        for i in range(c):
            nums.append(0)
        
        return nums
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna