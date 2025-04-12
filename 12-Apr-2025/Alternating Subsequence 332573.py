# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

using namespace std;
#include <bits/stdc++.h>

 
#define fast                      \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);
#define ll long long
#define int long long
#define db double
#define forr(n) for (int i = 0; i < n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define sort1(v) sort(v.begin(), v.end());
#define sort2(v) sort(v.begin(), v.end(),greater<int>());
#define uniquee(x) x.erase(unique(x.begin(), x.end()),x.end())
#define endl '\n'
#define PI acos(-1.0)
#define F(b)  fixed << setprecision(b) 


void solve()
{
    int x,l;
    cin>>x;
    priority_queue<int> p;
    cin>>l;
    bool f =true;
    if(l<0) f = false;
    p.push(l);
    int sum =0;
    for(int i=1;i<x;i++){
        cin>>l;
        if(l<0&&f||l>0&&!f){
            sum+=p.top();
            while (!p.empty())
            {
                p.pop();
            }
            f =!f;
        }
        p.push(l);
    }
    if(!p.empty())sum+=p.top();
    cout<<sum;

}
signed main()
{
    // #ifndef ONLINE_JUDGE
        // freopen("input.txt", "r", stdin);
        // freopen("output.txt", "w", stdout);
    // #endif
    fast;
    int t = 1;
    cin >> t;
    forr(t)
    {
        solve();
        // if (t)
            cout << endl;
    }
}



 