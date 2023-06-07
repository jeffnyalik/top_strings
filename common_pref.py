"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return
        size = len(strs)
        if(size == 0): return
        if(size == 1): return strs[0]
        strs.sort()

        end = min(len(strs[0]), len(strs[size - 1]))
        i = 0
        while i < end and strs[0][i] == strs[size - 1][i]:
            i+=1
        pre = strs[0][0:i]
        return pre
    

sol = Solution()
strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))
