""""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

class Solution:
    ## Sol 1 with O(N) space complexity
    def reverseWords(self, s:str)->str:
        if not s: return ""
        words = s.split(" ")
        res = []

        for word in words:
            res.insert(0, word)
        return " ".join(res).strip()
    
    ## Sol 2 with Constant space complexity
    def reverseWords2(self,  s:str) -> str:
        if not s: return 
        res = ""
        i = 0
        n = len(s)

        while i < n:
            while i < n and s[i] == " ": i+=1
            if i >= n: break
            j = i+1

            while j < n and s[j] != " ": j+=1
            subs = s[i:j]
            if len(res) == 0: res = subs
            else: res = (subs + " " + res)
            i = j+1
        
        return res


sol = Solution()
# s = "a good example"
# s = "  hello world  "
s = "the sky is blue"
# print(sol.reverseWords(s))
print(sol.reverseWords2(s))
