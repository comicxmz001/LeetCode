class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secretTable = {}
        guessTable = {}
        bulls = 0
        cows = 0
        for i in xrange(len(secret)):
        	if secret[i] == guess[i]:
        		bulls += 1
        		continue
    		# if not bull, then add to hash table
        	if not secret[i] in secretTable:
        		secretTable[secret[i]] = 1
        	else:
        		secretTable[secret[i]] += 1
        	if not guess[i] in guessTable:
        		guessTable[guess[i]] = 1
        	else:
        		guessTable[guess[i]] += 1

        # check hash table
        for key in guessTable.keys():
        	if key in secretTable.keys():
        		cows += min(guessTable[key],secretTable[key])

        return str(bulls)+"A"+str(cows)+"B"

if __name__ == "__main__":
	secret = ""
	guess = ""
	print Solution().getHint(secret,guess)
	tt ={x:0 for x in xrange(10)}
	print tt