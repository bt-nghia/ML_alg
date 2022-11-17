#include <bits/stdc++.h>

using namespace std;

int solve(vector<int> a) {
    int n = a.size();
    vector<int> dp(n, 0);
    for(int i = 0; i < n; i++) {
        dp[i] = a[i];
    }
    for(int i = 1; i < n; i++) {
        for(int j = 0; j < i; j++) {
            if(a[j] <= a[i]) {
                dp[i] = max(dp[i], dp[j] + a[i]);
            }
        }
    }
    int ans = 0;
    for(int i = 0; i < n; i++) {
        ans = max(ans, dp[i]);
    }
    return ans;
}

int main() {
    vector<int> a  = {1, 101, 2, 3, 100, 4, 5};
    cout << solve(a);
}