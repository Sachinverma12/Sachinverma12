class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        vowel=set('aeiouAEIOU')
        left = 0
        right=len(lst)-1
        while(left <= right):
            while(left<=right and lst[left] not in vowel):
                left+=1
            while(left<=right and lst[right] not in vowel):
                right-=1
            if (left>right):
                break
            lst[left],lst[right]= lst[right],lst[left]
            left+=1
            right-=1
        
        return ''.join(lst)
        