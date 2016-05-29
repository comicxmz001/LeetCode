class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        use a array to track the vowels position, then do the swap at these positions
        as string is immutable, convert string to list, then join back
        """
        vowels = 'aeiouAEIOU'
        vowelspos = [x for x, y in enumerate(s) if y in vowels ]
        s = list(s)

        low = 0
        high = len(vowelspos)-1
        while low < high:
        	s[vowelspos[low]],s[vowelspos[high]] = s[vowelspos[high]],s[vowelspos[low]]
        	low += 1
        	high -= 1
        return ''.join(s)


if __name__ == '__main__':
	s = 'l\oe'
	print Solution().reverseVowels(s)