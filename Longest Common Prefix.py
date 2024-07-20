class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        if not v:
            return ""
        
        v.sort()
        first, last = v[0], v[-1]
        i = 0
        
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]
        
