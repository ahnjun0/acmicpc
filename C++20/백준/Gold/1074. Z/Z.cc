#include <iostream>
using namespace std;

int recursive(int N, int r, int c) {
    if (N == 0) return 0;

    int half = 1 << (N - 1);

    if (r < half && c < half) return recursive(N - 1, r, c);
    else if (r < half && c >= half) return (half * half) + recursive(N - 1, r, c - half);
    else if (r >= half && c < half) return 2 * (half * half) + recursive(N - 1, r - half, c);
    else return 3 * (half * half) + recursive(N - 1, r - half, c - half);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, r, c;
    cin >> N >> r >> c;
    cout << recursive(N, r, c) << '\n';
    return 0;
}
