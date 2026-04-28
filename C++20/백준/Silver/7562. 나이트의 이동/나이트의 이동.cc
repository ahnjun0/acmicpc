#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int dx[8] = {2,2,-2,-2,1,1,-1,-1};
int dy[8] = {1,-1,1,-1,2,-2,2,-2};
int TC, l;


struct Point {
    int x, y;
    auto operator<=>(const Point&) const = default;
};

Point s, d;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> TC;
    
    for (int i = 0; i < TC; i++) {
        bool breakFlag = false;
        
        cin >> l;
        
        cin >> s.x >> s.y;
        cin >> d.x >> d.y;
        
        if (s == d) { // operator overloading, Same place
            cout << "0\n";
            continue;
        }
        
        vector<vector<int>> board(l, vector<int>(l, 0));
        queue<Point> q;
        Point point;
        
        board[s.x][s.y] = 1;
        
        q.push(s);
        
        while (!q.empty() && !breakFlag) {
            point = q.front(); q.pop();
            
            for (int n = 0; n < 8; n++) {
                int nx = point.x + dx[n];
                int ny = point.y + dy[n];
                
                if (0 <= nx && nx < l && 0 <= ny && ny < l && board[nx][ny] == 0) {

                    if (nx == d.x && ny == d.y) {
                        cout << board[point.x][point.y] << "\n";
                        breakFlag = true;
                        break;
                    }
                    
                    board[nx][ny] = board[point.x][point.y] + 1;
                    q.push({nx, ny});
                }
            }
        }
 
    }
    
    return 0;
}