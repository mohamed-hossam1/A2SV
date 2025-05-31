# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    # your code goes here
    s,k = 0,0
    n = len(string)
    for i in range(n):
        if string[i] in ['A','E','I','O','U']:
            k+=(n-i)
        else:
            s+=(n-i)
    if s > k:
        print('Stuart',s)
    elif k>s:
        print('Kevin',k)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)