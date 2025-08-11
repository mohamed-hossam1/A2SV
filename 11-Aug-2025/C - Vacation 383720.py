# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

def main():
    n = int(input())
    v = [(0, 0, 0)]  

    for _ in range(n):
        a, b, c = map(int, input().split())
        v.append((a, b, c))

    dp = [[0] * 3 for _ in range(n + 1)]

    dp[1][0] = v[1][0]
    dp[1][1] = v[1][1]
    dp[1][2] = v[1][2]

    for i in range(2, n + 1):
        dp[i][0] = v[i][0] + max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = v[i][1] + max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = v[i][2] + max(dp[i - 1][0], dp[i - 1][1])

    print(max(dp[n][0], dp[n][1], dp[n][2]))

if __name__ == "__main__":
    main()
