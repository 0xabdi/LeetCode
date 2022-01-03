class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x = str(x)
        x_reverse = x[::-1]

        if(x == x_reverse):
            return True
        else:
            return False
