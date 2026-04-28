#include <bits/stdc++.h>
using namespace std;

int N;
int global_max_val = 0;

using Board = int[20][20];

inline void copyBoard(const Board src, Board dest) {
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            dest[i][j] = src[i][j];
}

inline int getMaxTile(const Board b) {
    int m = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            m = max(m, b[i][j]);
    return m;
}

bool moveLeft(const Board b, Board res) {
    bool changed = false;
    for (int i = 0; i < N; i++) {
        int idx = 0, last = 0;
        for (int j = 0; j < N; j++) res[i][j] = 0;
        for (int j = 0; j < N; j++) {
            if (b[i][j] == 0) continue;
            if (last == 0) {
                last = b[i][j];
            } else if (last == b[i][j]) {
                res[i][idx++] = last * 2;
                last = 0;
                changed = true;
            } else {
                res[i][idx++] = last;
                last = b[i][j];
            }
        }
        if (last != 0) res[i][idx++] = last;
        for (int j = 0; j < N; j++)
            if (res[i][j] != b[i][j]) changed = true;
    }
    return changed;
}

bool moveRight(const Board b, Board res) {
    bool changed = false;
    for (int i = 0; i < N; i++) {
        int idx = N - 1, last = 0;
        for (int j = 0; j < N; j++) res[i][j] = 0;
        for (int j = N - 1; j >= 0; j--) {
            if (b[i][j] == 0) continue;
            if (last == 0) {
                last = b[i][j];
            } else if (last == b[i][j]) {
                res[i][idx--] = last * 2;
                last = 0;
                changed = true;
            } else {
                res[i][idx--] = last;
                last = b[i][j];
            }
        }
        if (last != 0) res[i][idx--] = last;
        for (int j = 0; j < N; j++)
            if (res[i][j] != b[i][j]) changed = true;
    }
    return changed;
}

bool moveUp(const Board b, Board res) {
    bool changed = false;
    for (int j = 0; j < N; j++) {
        int idx = 0, last = 0;
        for (int i = 0; i < N; i++) res[i][j] = 0;
        for (int i = 0; i < N; i++) {
            if (b[i][j] == 0) continue;
            if (last == 0) {
                last = b[i][j];
            } else if (last == b[i][j]) {
                res[idx++][j] = last * 2;
                last = 0;
                changed = true;
            } else {
                res[idx++][j] = last;
                last = b[i][j];
            }
        }
        if (last != 0) res[idx++][j] = last;
        for (int i = 0; i < N; i++)
            if (res[i][j] != b[i][j]) changed = true;
    }
    return changed;
}

bool moveDown(const Board b, Board res) {
    bool changed = false;
    for (int j = 0; j < N; j++) {
        int idx = N - 1, last = 0;
        for (int i = 0; i < N; i++) res[i][j] = 0;
        for (int i = N - 1; i >= 0; i--) {
            if (b[i][j] == 0) continue;
            if (last == 0) {
                last = b[i][j];
            } else if (last == b[i][j]) {
                res[idx--][j] = last * 2;
                last = 0;
                changed = true;
            } else {
                res[idx--][j] = last;
                last = b[i][j];
            }
        }
        if (last != 0) res[idx--][j] = last;
        for (int i = 0; i < N; i++)
            if (res[i][j] != b[i][j]) changed = true;
    }
    return changed;
}

void dfs(const Board b, int depth) {
    int cur_max = getMaxTile(b);
    global_max_val = max(global_max_val, cur_max);

    if (depth == 5) return;

    Board tmp;

    if (moveLeft(b, tmp)) dfs(tmp, depth + 1);
    if (moveRight(b, tmp)) dfs(tmp, depth + 1);
    if (moveUp(b, tmp)) dfs(tmp, depth + 1);
    if (moveDown(b, tmp)) dfs(tmp, depth + 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    Board board;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> board[i][j];

    dfs(board, 0);
    cout << global_max_val << "\n";
    return 0;
}
