#include <iostream>

using namespace std;
int N, M;
int arr[9];
bool isUsed[9];

void func(int k) {
    if (k == M) {
        for (int i = 0; i < M; i++) {
            cout << arr[i] << ' ';;
            
        };
        cout << "\n"; return;
    }
    
    for (int i = 1; i <= N; i++) {
        if (!isUsed[i]) {
            arr[k] = i;
            isUsed[i] = 1;
            func(k + 1);
            isUsed[i] = 0;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    
    func(0);
    return 0;
}