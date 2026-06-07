class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        guide_word = strs[0]
        
        for i in range(len(guide_word)):
            char_to_check = guide_word[i]
            
            for next_word in strs[1:]:
                if i >= len(next_word) or next_word[i] != char_to_check:
                    return guide_word[:i] 
                    
        return guide_word  
        
            