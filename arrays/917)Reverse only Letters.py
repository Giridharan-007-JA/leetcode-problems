'''Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l=list(s)
        i=0
        j=len(l)-1

        while i<j:
            if l[i].isalpha() and l[j].isalpha():
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            elif not l[i].isalpha():
                i+=1
            elif not l[j].isalpha():
                j-=1
        return "".join(l)