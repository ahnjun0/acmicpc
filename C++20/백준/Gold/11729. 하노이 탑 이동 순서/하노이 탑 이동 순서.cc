#include <iostream>
using namespace std;

void hanoi(int num, int now, int stopover, int togo) {
    if (num == 1) {
        cout << now << " " << togo << '\n';
    } else {
        hanoi(num - 1, now, togo, stopover);
        cout << now << " " << togo << '\n';
        hanoi(num - 1, stopover, now, togo);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    cout << (1 << N) - 1 << '\n';
    hanoi(N, 1, 2, 3);

    return 0;
}
