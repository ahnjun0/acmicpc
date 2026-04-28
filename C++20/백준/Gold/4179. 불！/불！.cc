#include <iostream>
#include <queue>
#include <string>

using namespace std;

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int fireTime[1000][1000];
int mazeTime[1000][1000];

int R, C;

struct Point {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

	cin >> R >> C;
	
	queue<Point> q;
	queue<Point> jq;
	
	for (int i = 0; i < R; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < C; j++) {
            if (row[j] == '#') {
                fireTime[i][j] = -1;
                mazeTime[i][j] = -1;
            }
            else if (row[j] == 'F') {
                q.push({i, j});
                fireTime[i][j] = 1;
            } else if (row[j] == 'J') {
                jq.push({i, j});
                mazeTime[i][j] = 1;
            }
        }
    }
    
    Point point;
    
    // fireTime
    while (!q.empty()) {
        point = q.front(); q.pop();

        for (int d = 0; d < 4; d++) {
            int nx = point.x + dx[d];
            int ny = point.y + dy[d];

            if (0 <= nx && nx < R && 0 <= ny && ny < C && fireTime[nx][ny] == 0) {
                fireTime[nx][ny] = fireTime[point.x][point.y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    
    // mazeTime (Jihoon-Time)
    while (!jq.empty()) {
        point = jq.front(); jq.pop();
        
        // edge_case
        if (point.x == 0 || point.x == R-1 || point.y == 0 || point.y == C-1) {
            cout << mazeTime[point.x][point.y];
            return 0;
        }

        for (int d = 0; d < 4; d++) {
            int nx = point.x + dx[d];
            int ny = point.y + dy[d];

            if (0 <= nx && nx < R && 0 <= ny && ny < C && mazeTime[nx][ny] == 0 && (fireTime[nx][ny] == 0 || (fireTime[nx][ny] > (mazeTime[point.x][point.y] + 1)))) {
                mazeTime[nx][ny] = mazeTime[point.x][point.y] + 1;
                

                if (nx == 0 || nx == R-1 || ny == 0 || ny == C-1) {
                    cout << mazeTime[nx][ny];
                    return 0;
                }

                
                jq.push({nx, ny});
                
            }
        }
    }
    
    
    cout << "IMPOSSIBLE";

    
    return 0;
}
