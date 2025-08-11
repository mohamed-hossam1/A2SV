# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

def main():
    n = int(input())
    h = list(map(int, input().split()))

    dp = [0] * (n + 1)
    
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])

    for i in range(2, n):
        op1 = dp[i-1] + abs(h[i] - h[i-1])
        op2 = dp[i-2] + abs(h[i] - h[i-2])
        dp[i] = min(op1, op2)

    print(dp[n-1])

if __name__ == "__main__":
    main()
