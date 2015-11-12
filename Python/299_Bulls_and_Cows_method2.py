class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # this is actually slower than method 1, which does not use mapping function to create dictionary.
        secretTable = {x:0 for x in xrange(10)}
        guessTable = {x:0 for x in xrange(10)}
        bulls = 0
        cows = 0
        for i in xrange(len(secret)):
        	if secret[i] == guess[i]:
        		bulls += 1
        		continue
    		# if not bull, then add to hash table
        	secretTable[int(secret[i])] += 1
        	guessTable[int(guess[i])] += 1

        # check hash table
        for key in guessTable.keys():
        	if key in secretTable.keys():
        		cows += min(guessTable[key],secretTable[key])

        return str(bulls)+"A"+str(cows)+"B"

if __name__ == "__main__":
	secret = "1807"
	guess = "7801"
	print Solution().getHint(secret,guess)
