# Note: Python2.x stores the keys in unicode characters
#{u'b': 1}
#{u'a': 1}

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rDict = {}
        mDict = {}

        #counting the occurances of letters in ransomNote
        for letter in ransomNote:
            if letter not in rDict:
                rDict[letter] = ransomNote.count(letter)

        #counting the occurances of letters in magazine
        for letter in magazine:
            if letter not in mDict:
                mDict[letter] = magazine.count(letter)

        for key in rDict:
            if key not in mDict:
                return False
            elif rDict[key]>mDict[key]:
                return False
        
        return True
