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

struct MoveResult {
    bool moved;
    bool merged;
};


MoveResult moveLeft(const Board b, Board res) {
    bool moved = false, merged = false;
    for (int i = 0; i < N; i++) {
        int idx = 0;
        int last = -1;
        for (int j = 0; j < N; j++) res[i][j] = -1;

        for (int j = 0; j < N; j++) {
            if (b[i][j] == -1) continue;
            if (last == -1) {
                last = b[i][j];
            } else if (last == b[i][j]) {
                res[i][idx++] = last + 1; // merge
                last = -1;
                moved = merged = true;
            } else {
                res[i][idx++] = last;
                last = b[i][j];
            }
        }
        if (last != -1) res[i][idx++] = last;

        for (int j = 0; j < N; j++) {
            if (res[i][j] != b[i][j]) moved = true;
        }
    }
    return {moved, merged};
}

MoveResult moveRight(const Board b, Board res) {
    bool moved = false, merged = false;
    for (int i = 0; i < N; i++) {
        int idx = N - 1;
        int last = -1;
        for (int j = 0; j < N; j++) res[i][j] = -1;

        for (int j = N - 1; j >= 0; j--) {
            if (b[i][j] == -1) continue;
            if (last == -1) {
                last = b[i][j];
            } else if (last == b[i][j]) {
                res[i][idx--] = last + 1;
                last = -1;
                moved = merged = true;
            } else {
                res[i][idx--] = last;
                last = b[i][j];
            }
        }
        if (last != -1) res[i][idx--] = last;

        for (int j = 0; j < N; j++) {
            if (res[i][j] != b[i][j]) moved = true;
        }
    }
    return {moved, merged};
}

MoveResult moveUp(const Board b, Board res) {
    bool moved = false, merged = false;
    for (int j = 0; j < N; j++) {
        int idx = 0;
        int last = -1;
        for (int i = 0; i < N; i++) res[i][j] = -1;

        for (int i = 0; i < N; i++) {
            if (b[i][j] == -1) continue;
            if (last == -1) {
                last = b[i][j];
            } else if (last == b[i][j]) {
                res[idx++][j] = last + 1;
                last = -1;
                moved = merged = true;
            } else {
                res[idx++][j] = last;
                last = b[i][j];
            }
        }
        if (last != -1) res[idx++][j] = last;

        for (int i = 0; i < N; i++) {
            if (res[i][j] != b[i][j]) moved = true;
        }
    }
    return {moved, merged};
}

MoveResult moveDown(const Board b, Board res) {
    bool moved = false, merged = false;
    for (int j = 0; j < N; j++) {
        int idx = N - 1;
        int last = -1;
        for (int i = 0; i < N; i++) res[i][j] = -1;

        for (int i = N - 1; i >= 0; i--) {
            if (b[i][j] == -1) continue;
            if (last == -1) {
                last = b[i][j];
            } else if (last == b[i][j]) {
                res[idx--][j] = last + 1;
                last = -1;
                moved = merged = true;
            } else {
                res[idx--][j] = last;
                last = b[i][j];
            }
        }
        if (last != -1) res[idx--][j] = last;

        for (int i = 0; i < N; i++) {
            if (res[i][j] != b[i][j]) moved = true;
        }
    }
    return {moved, merged};
}

void dfs(const Board b, int depth, int last_horizontal_merge, int last_vertical_merge) {
    int cur_max = getMaxTile(b);
    global_max_val = max(global_max_val, cur_max);

    if (depth == 10) return;

    Board tmp;
    MoveResult result;

    // Left
    result = moveLeft(b, tmp);
    if (result.moved) {
        if (result.merged || last_horizontal_merge != depth - 1) {
            dfs(tmp, depth + 1, result.merged ? depth : last_horizontal_merge, last_vertical_merge);
        }
    }

    // Right
    result = moveRight(b, tmp);
    if (result.moved) {
        if (result.merged || last_horizontal_merge != depth - 1) {
            dfs(tmp, depth + 1, result.merged ? depth : last_horizontal_merge, last_vertical_merge);
        }
    }

    // Up
    result = moveUp(b, tmp);
    if (result.moved) {
        if (result.merged || last_vertical_merge != depth - 1) {
            dfs(tmp, depth + 1, last_horizontal_merge, result.merged ? depth : last_vertical_merge);
        }
    }

    // Down
    result = moveDown(b, tmp);
    if (result.moved) {
        if (result.merged || last_vertical_merge != depth - 1) {
            dfs(tmp, depth + 1, last_horizontal_merge, result.merged ? depth : last_vertical_merge);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    Board board;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            int x; cin >> x;
            if (x == 0) board[i][j] = -1;
            else board[i][j] = __lg(x); // log2
        }

    dfs(board, 0, -2, -2);
    cout << (1 << global_max_val) << "\n";
    return 0;
}