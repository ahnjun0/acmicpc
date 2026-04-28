#include <iostream>
#include <queue>

using namespace std;


int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int tomatoes[1000][1000];
int N, M;
int cnt_zero;

struct Point {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

	cin >> M >> N;
	
	queue<Point> q;
	

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> tomatoes[i][j];
            if (tomatoes[i][j] == 1) {
                q.push({i, j});
            } else if (tomatoes[i][j] == 0) {
                cnt_zero++;
            }
        }
    }
    
    
    Point point;
    
    
    while (!q.empty()) {
        point = q.front(); q.pop();

        for (int d = 0; d < 4; d++) {
            int nx = point.x + dx[d];
            int ny = point.y + dy[d];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M && tomatoes[nx][ny] == 0) {
                tomatoes[nx][ny] = tomatoes[point.x][point.y] + 1; // 이전 거리 + 1
                q.push({nx, ny});
                cnt_zero--;
            }
        }
    }
    
    if (cnt_zero > 0) {
        cout << -1 << '\n';
    } else {
        int result = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (tomatoes[i][j] > result) result = tomatoes[i][j];
            }
        }
        cout << result - 1 << '\n';
    }
    
    return 0;
}