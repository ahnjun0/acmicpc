#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string b;
	char before = '\0';
	stack<char> st;
	int plus = 0, multi = 1;
	
	cin >> b;

	for (auto s : b) {
	    switch ((int)s) {
	        case (int)'(':
	            st.push(s);
	            multi *= 2;
	            break;

            case (int)'[':
                st.push(s);
                multi *= 3;
                break;
                
            case (int)')':
                if (st.empty() || st.top() == '[') {
                    cout << 0; return 0;
                } else if (before == '(') plus += multi;
                multi /= 2;
                st.pop();
                break;
                
            case (int)']':
                if (st.empty() || st.top() == '(') {
                    cout << 0; return 0;
                } else if (before == '[') plus += multi;
                multi /= 3;
                st.pop();
                break;
	    }
	    
	    before = s;
	}
	
	if (!st.empty()) cout << 0;
	else cout << plus;
	
}