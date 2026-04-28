#include <iostream>
#include <queue>

using namespace std;

bool visited[100001];
int N, K;

struct Point {
    int pos, dist;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
	cin >> N >> K;
	
	queue<Point> q;
	Point point;

    q.push({N, 0});
    visited[N] = true;
    
    while (!q.empty()) {
        point = q.front(); q.pop();

        if (point.pos == K) {
            cout << point.dist << '\n';
            return 0;
        }

        int next_positions[] = {point.pos - 1, point.pos + 1, point.pos * 2};
        for (int next : next_positions) {
            if (0 <= next && next <= 100000 && !visited[next]) {
                visited[next] = true;
                q.push({next, point.dist + 1});
            }
        }
    }
    
    return 0;
}