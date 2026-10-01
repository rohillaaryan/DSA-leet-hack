class Solution(object):
    def missingNumber(self, nums):
        

        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna