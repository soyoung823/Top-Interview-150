"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        #print(r_counter)
        #print(m_counter)
        for ch, count in r_counter.items():
            if ch not in m_counter:
                return False
            # in m_counter
            if count > m_counter[ch]:
                return False
            # <=
            m_counter[ch] -= count
        return True

# TC: O(n) SC: O(n)
