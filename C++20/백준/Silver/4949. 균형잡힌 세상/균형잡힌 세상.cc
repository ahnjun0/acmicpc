#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    
    while (true) {
        string bal;
        getline(cin, bal);
        if (bal == ".") break;
        
        stack<char> st;
        bool isValid = true;
        
        for (auto s : bal) {
            if (s == '[' || s == '(') st.push(s);
            else if (s == ']' || s == ')') {
                if (!st.empty() && ((st.top() == '[' && s == ']') || (st.top() == '(' && s == ')'))) st.pop();
                else {
                    isValid = false;
                    break;
                }
            }
        }
        
        if (!st.empty()) isValid = false;
        cout << (isValid ? "yes\n" : "no\n");
    }
}