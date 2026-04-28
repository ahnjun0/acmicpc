#include <iostream>

using namespace std;

int N;
int arr[20];
bool possible[2000001];

void solve(int idx, int sum) {
    if (idx == N) {
        if (sum > 0) possible[sum] = true;
        return;
    }

    solve(idx+1, sum + arr[idx]);
    solve(idx+1, sum);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    
    for (int i = 0; i < N; i++) cin >> arr[i];
    solve(0, 0);
    

    for (int i = 1; i <= 2000000; i++) {
        if (!possible[i]) {
            cout << i;
            return 0;
        }
    }
    
    return 0;
}