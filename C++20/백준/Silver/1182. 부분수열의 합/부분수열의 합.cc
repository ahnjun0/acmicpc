#include <iostream>

using namespace std;

int N, S, cnt;
int arr[20];

void solve(int idx, int sum) {
    if (idx == N) return;
    if (sum + arr[idx] == S) cnt++;
    
    solve(idx+1, sum + arr[idx]);
    solve(idx+1, sum);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> S;
    
    for (int i = 0; i < N; i++) cin >> arr[i];
    solve(0, 0);
    
    cout << cnt;
    
    return 0;
}