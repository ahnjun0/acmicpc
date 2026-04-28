#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string str;
    cin >> str;

    stack<char> left_stack;
    vector<char> right_stack;

    for (char c : str) {
        left_stack.push(c);
    }

    int m;
    cin >> m;
    while (m--) {
        string cmd;
        cin >> cmd;

        if (cmd == "L") {
            if (!left_stack.empty()) {
                right_stack.push_back(left_stack.top());
                left_stack.pop();
            }
        }
        else if (cmd == "D") {
            if (!right_stack.empty()) {
                left_stack.push(right_stack.back());
                right_stack.pop_back();
            }
        }
        else if (cmd == "B") {
            if (!left_stack.empty()) {
                left_stack.pop();
            }
        }
        else if (cmd == "P") {
            char ch;
            cin >> ch;
            left_stack.push(ch);
        }
    }

    string result;
    stack<char> temp;
    while (!left_stack.empty()) {
        temp.push(left_stack.top());
        left_stack.pop();
    }
    while (!temp.empty()) {
        result += temp.top();
        temp.pop();
    }

    for (auto it = right_stack.rbegin(); it != right_stack.rend(); ++it) {
        result += *it;
    }

    cout << result << '\n';
    return 0;
}
