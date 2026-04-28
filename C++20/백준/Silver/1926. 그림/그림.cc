#include <iostream>
#include <utility>
#include <queue>

using namespace std;
#define X first
#define Y second
int board[502][502];
bool visited[502][502];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int n, m;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

	cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }
    
    int maxPaint = 0;
    int numPaint = 0;
    
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 0 || visited[i][j]) continue;
            numPaint++;
            
            queue<pair<int, int>> que;
            visited[i][j] = true;
            
            que.push({i, j});
            int nowPaint = 0;
            while (!que.empty()) {
                nowPaint++;
                auto point = que.front(); que.pop();
                for (int d = 0; d < 4; d++) {
                    int nx = point.X + dx[d];
                    int ny = point.Y + dy[d];
                    
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    if (visited[nx][ny] || board[nx][ny] != 1) continue;
                    visited[nx][ny] = 1;
                    que.push({nx, ny});
                }
            }
            
            maxPaint = max(nowPaint, maxPaint);
        }
    }
    
    cout << numPaint << "\n" << maxPaint;
    
    return 0;
}
