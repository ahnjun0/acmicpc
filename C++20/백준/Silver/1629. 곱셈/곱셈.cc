#include <iostream>

using namespace std;
using ll = long long;

ll power(ll A, ll B, ll C) {
    if (B == 1) {
        return A % C;
    } 
    ll half = power(A, B / 2, C) % C;
    half = (half * half) % C;
    
    if ((B & 1) == 0) return half;
    
    return (half *(A % C)) % C;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll A, B, C;
    cin >> A >> B >> C;
    cout << power(A, B, C) << "\n";
    
    return 0;
}