#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while (t--) {
        long long n;
        cin >> n;
        
        if (n % 2 == 1) {
            cout << -1 << endl;
        } else {
            cout << 1 << " " << n / 2 << endl;
        }
    }
    
    return 0;
}

