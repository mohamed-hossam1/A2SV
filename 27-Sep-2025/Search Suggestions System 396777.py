# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans=[]
        for i in range(1,len(searchWord)+1):
            products = [p for p in products if p.startswith(searchWord[:i])]
            ans.append(products[:3])
        return ans
