#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N;

    cout << (N * (N + 1) * (N + 2))/2;

    return 0;
}