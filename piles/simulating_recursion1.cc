#include <iostream>
using namespace std;

void work(int n) {
    if (n > 0) {
        cout << ' ' << n;
        work(n - 1);
        work(n - 1);
    }
}

int main() {
    int n;
    while (cin >> n) {
        work(n);
        cout << endl;
    }
    return 0;
}