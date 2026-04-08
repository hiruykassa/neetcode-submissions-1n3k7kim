class Solution:
    def makeWordHashmap(self, word):
        letters = {}             
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        return letters
        
    def groupMatching(self, words):
        arrayWithGroups = []
        #loop through words
        for word in words:
            # have we seen the value
            seen = False
            for i, group in enumerate(arrayWithGroups):
                # if we seen word alrdy add it to that group
                if word[1] == group[0]:
                    arrayWithGroups[i].append(word[0])
                    seen = True
            # if not make group for it
            if not seen:
                arrayWithGroups.append([word[1], word[0]])
        # remove beginning of each group
        for i in range(len(arrayWithGroups)):
            arrayWithGroups[i].pop(0)
        return arrayWithGroups
        

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = [] # [Word, LettersHashmap]
        # hashmap for each word 
        for word in strs:
            # create my hashmap
            letters = self.makeWordHashmap(word)
            # add words to hashmap
            words.append([word, letters])
        return self.groupMatching(words)
        
