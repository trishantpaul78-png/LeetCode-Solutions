class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Initialize your two boundary scouts
        l = 0
        r = len(s) - 1

        # Step 2: Loop until the pointers meet or cross in the middle
        while l < r:
            
            # Step 3: Skip non-alphanumeric characters from the left
            while l < r and not s[l].isalnum():
                l += 1
                
            # Skip non-alphanumeric characters from the right
            while l < r and not s[r].isalnum():
                r -= 1

            # Step 4: Compare the valid characters in lowercase
            if s[l].lower() != s[r].lower():
                return False  # Instant exit if a mismatch is found

            # Step 5: Move pointers inward to check the next pair
            l += 1
            r -= 1

        # If we made it through the loop safely, it's a valid palindrome!
        return True
        
        