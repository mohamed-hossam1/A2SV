# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a: int, b: int) -> None:
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return
        if self.r[pa] < self.r[pb]:
            self.p[pa] = pb
        elif self.r[pb] < self.r[pa]:
            self.p[pb] = pa
        else:
            self.p[pb] = pa
            self.r[pa] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_id = {}
        email_name = {}
        eid = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in email_id:
                    email_id[email] = eid
                    eid += 1
                email_name[email] = name

        dsu = DSU(eid)
        for acc in accounts:
            if len(acc) <= 2:  
                continue
            base = email_id[acc[1]]
            for email in acc[2:]:
                dsu.union(base, email_id[email])
        groups = defaultdict(list)
        for email, i in email_id.items():
            root = dsu.find(i)
            groups[root].append(email)

        res = []
        for emails in groups.values():
            emails.sort()
            name = email_name[emails[0]]
            res.append([name] + emails)
        return res
