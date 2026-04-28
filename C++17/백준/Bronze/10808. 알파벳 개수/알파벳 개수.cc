#include <bits/stdc++.h>
using namespace std;

int seq[26];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    string s;
    cin >> s;
    
    for (auto c : s) {
        seq[c-97]++;
    }
    
    for (int i = 0; i < 26; i++) {
        cout << seq[i] << ' ';
    }
}
