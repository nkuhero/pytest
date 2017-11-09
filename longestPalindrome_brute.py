#暴力穷举法
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if self.isPalindrome(s[i:j+1]) and len(s[i:j+1]) > len(longest):
                    longest = s[i:j+1]
        return longest


    def isPalindrome(self, s):
        l = len(s)
        if l % 2 == 1:
            for i in range(int(l / 2) + 1):
                if s[i] != s[l-i-1]:
                    return False
            return True

        if l % 2 == 0:
            for i in range(int(l / 2)):
                if s[i] != s[l-i-1]:
                    return False
            return True
