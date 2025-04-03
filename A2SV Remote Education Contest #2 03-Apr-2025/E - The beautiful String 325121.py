# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

ii = lambda: int(input())
il = lambda: list(map(int, input().split()))
isc = lambda: list(input())

for _ in range(ii()):
    s = isc()
    q = ii()

    def is_1100_at(i):
        return i >= 0 and i + 3 < len(s) and s[i] == '1' and s[i+1] == '1' and s[i+2] == '0' and s[i+3] == '0'

    count = sum(1 for i in range(len(s) - 3) if is_1100_at(i))

    for _ in range(q):
        idx, val = il()
        idx -= 1
        val = str(val)

        if s[idx] == val: 
            print("YES" if count else "NO")
            continue

        for i in range(idx - 3, idx + 1):
            if is_1100_at(i):
                count -= 1

        s[idx] = val

        for i in range(idx - 3, idx + 1):
            if is_1100_at(i):
                count += 1

        print("YES" if count else "NO")
