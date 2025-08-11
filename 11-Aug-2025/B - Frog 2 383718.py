# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    
    dp = [0] * (n + 1)

    dp[0] = 0

    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(i-1, -1, -1):
            if i - j > k:
                break
            dp[i] = min(dp[i], abs(h[i] - h[j]) + dp[j])

    print(dp[n-1])

if __name__ == "__main__":
    main()
