class Solution:   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a dict"
        seen = {}
        #iterate between str
        for word in strs:
            #sort the list into the key
            key = ''.join(sorted(word))
            #check if the key exists in seen
            if key in seen:
                #if it does append to it
                seen[key].append(word)
                #else create a new group
            else:
                seen[key] = [word]
            #return the value of the word
        return list(seen.values())