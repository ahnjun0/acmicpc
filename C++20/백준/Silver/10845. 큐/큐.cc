#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    queue<int> q;
    
    int N, inp;
    string cmd;
    cin >> N;
    
    while (N--) {
        cin >> cmd;
        
        if (cmd == "push") {
            cin >> inp;
            q.push(inp);
        } else if (cmd == "pop") {
            if (q.empty()) cout << -1 << "\n";
            else {
                cout << q.front() << "\n";
                q.pop();
            }
        } else if (cmd == "size") {
            cout << q.size() << "\n";
        } else if (cmd == "empty") {
            cout << ((q.empty()) ? 1 : 0) << "\n";
        } else if (cmd == "front") {
            cout << ((q.empty()) ? -1 : q.front()) << "\n";
        } else { // cmd == "back" 
            cout << ((q.empty()) ? -1 : q.back()) << "\n";
        }
    }
    
    return 0;
}