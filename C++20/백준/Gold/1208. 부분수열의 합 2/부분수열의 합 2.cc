#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, S, cnt;
vector<int> arr;


void solve(const auto& seq, int idx, int sum, auto& sums) {
    if (idx == (int)seq.size()) {
        sums.push_back(sum);
        return;
    }
    solve(seq, idx + 1, sum + seq[idx], sums);
    solve(seq, idx + 1, sum, sums);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> S;
    arr.resize(N);
    for (int i = 0; i < N; i++) cin >> arr[i];

    vector<int> left(arr.begin(), arr.begin() + N/2);
    vector<int> right(arr.begin() + N/2, arr.end());

    vector<int> leftSums, rightSums;
    solve(left, 0, 0, leftSums);
    solve(right, 0, 0, rightSums);

    sort(rightSums.begin(), rightSums.end());

    long long cnt = 0;
    for (int ls : leftSums) {
        int target = S - ls;
        auto range = equal_range(rightSums.begin(), rightSums.end(), target);
        cnt += (range.second - range.first);
    }

    // 공집합 제외
    if (S == 0) cnt -= 1;

    cout << cnt;
    return 0;
}