#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    stack<int> s;
    
    int N, inp;
    string cmd;
    cin >> N;
    
    while (N--) {
        cin >> cmd;
        
        if (cmd == "push") {
            cin >> inp;
            s.push(inp);
        } else if (cmd == "pop") {
            if (s.empty()) cout << -1 << "\n";
            else {
                cout << s.top() << "\n";
                s.pop();
            }
        } else if (cmd == "size") {
            cout << s.size() << "\n";
        } else if (cmd == "empty") {
            cout << ((s.empty()) ? 1 : 0) << "\n";
        } else { // cmd == "top" 
            cout << ((s.empty()) ? -1 : s.top()) << "\n";
        }
    }
    
    return 0;
}