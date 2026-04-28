#include <iostream>
#include <queue>
#include <string>

using namespace std;


int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int maze[100][100];
int N, M;

struct Point {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

	cin >> N >> M;

    for (int i = 0; i < N; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < M; j++) {
            maze[i][j] = row[j] - '0';
        }
    }
    
    queue<Point> q;
    Point point;
    
    q.push({0, 0});
    
    
    while (!q.empty()) {
        point = q.front(); q.pop();

        for (int d = 0; d < 4; d++) {
            int nx = point.x + dx[d];
            int ny = point.y + dy[d];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M && maze[nx][ny] == 1) {
                maze[nx][ny] = maze[point.x][point.y] + 1; // 이전 거리 + 1
                q.push({nx, ny});
            }
        }
    }
    
    cout << maze[N-1][M-1];
    
    return 0;
}
