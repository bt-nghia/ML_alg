#include <bits/stdc++.h>

using namespace std;

int minwalk(vector<vector<int>> &forest, int r, int c, int dr, int dc, vector<vector<bool>> mt) {
    if(r == dr && c == dc) {
        return 0;
    }
    
    if( r < 0 || c < 0 || r >= forest.size() || c >= forest[0].size() || forest[r][c] == 0 || mt[r][c] == true) { 
        return 7*(forest.size() + forest[0].size());
    }
    
    else {
        mt[r][c] = true;
        int x = minwalk(forest, r+1, c, dr, dc, mt);
        int xx = minwalk(forest, r, c+1, dr, dc, mt);
        int y = minwalk(forest, r-1, c, dr, dc, mt);
        int yy = minwalk(forest, r, c-1, dr, dc, mt);
        return min(min(x, y), min(xx, yy)) + 1;
    }
}

int cutOffTree(vector<vector<int>>& forest) {
    int m = forest.size();
    int n = forest[0].size();
    vector<vector<int>> mp;
    for(int i = 0; i < forest.size(); i++) {
        for(int j = 0; j < forest[0].size(); j++) {
            if(forest[i][j] != 0) {
                mp.push_back({forest[i][j], i, j});
            }
        }
    }
    sort(mp.begin(), mp.end());
    int ans = 0;
    int startr = 0;
    int startc = 0;
    vector<vector<bool>> mt(m, vector<bool> (n, false));
    for(auto i : mp) {
        int step = minwalk(forest, startr, startc, i[1], i[2], mt);
        if(step >= 7*(m + n)) {
            return -1;
        }
        ans+=step;
        startr = i[1];
        startc = i[2];
    }
    return ans;
}

int main() {;
    
}