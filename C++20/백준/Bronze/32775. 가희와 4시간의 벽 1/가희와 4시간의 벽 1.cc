#include <bits/stdc++.h>
using namespace std;

int s, f;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> s;
    cin >> f;
    
    cout << ((s > f) ? "flight" : "high speed rail");

    return 0;
}