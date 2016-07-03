class Solution(object):
		def isPalindrome(self, s):
			"""
			:type s: str
			:rtype: bool
			"""
			
			l,r = 0, len(s)-1
			
			while l < r:
				while l < r and not s[l].isalnum(): l += 1
				while l < r and not s[r].isalnum(): r -= 1
				
				if s[l].lower() != s[r].lower():
					return False
				else:
					l += 1
					r -= 1
			return True
			
if __name__ == "__main__":
	s = "a."
	print Solution().isPalindrome(s)