# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:

        folders = path.split('/')
        res = []
        print(folders)

        for i, f in enumerate(folders):
            if i == 0 and f == '': res.append('/')
            elif f == '..':
                if len(res) >2:
                    res = res[:-2]
            elif f == '.':
                continue
            elif f not in ['/','//', '']:
                res.append(f)
                res.append('/')
            print(i, f, res)
        if len(res) > 1: res=res[:-1]
        return ''.join(res)