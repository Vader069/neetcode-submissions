class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1=[0]*26
        freq2=[0]*26
        for x in s:
            freq1[ord(x)-ord('a')]+=1
        for y in t:
            freq2[ord(y)-ord('a')]+=1
        if(freq1==freq2):
            return True
        else:
            return False
        