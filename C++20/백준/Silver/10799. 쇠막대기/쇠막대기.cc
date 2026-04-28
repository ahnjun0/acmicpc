#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string b;
	int cnt = 0;
	cin >> b;
	stack<char> st;
    for (int i = 0; i < b.length(); ++i) {
        char s = b[i];
        
        if (s == '(') {
            st.push(s);
        }
        else { // s == ')'
            if (b[i-1] == '(') { // laser
                st.pop();
                cnt += st.size();
            }
            else {
                st.pop();
                cnt++;
            }
        }
    }

	cout << cnt;
}