#include <iostream>

using namespace std;
int N, cnt;


void queen(int row, int col_mask, int diag1_mask, int diag2_mask) {
    if (row == N) {
        cnt++;
        return;
    }

    // col_mask | diag1_mask | diag2_mask -> The current queen's position
    int available = ((1 << N) - 1) & ~(col_mask | diag1_mask | diag2_mask);

    while (available) {
        int pos = available & -available; // lowbit -> Queen's position
        available &= ~pos;

        queen(row + 1,
              col_mask | pos,
              (diag1_mask | pos) << 1,
              (diag2_mask | pos) >> 1);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    
    queen(0,0,0,0);
    
    cout << cnt;
    return 0;
}