#include <iostream>
#include <functional>
#include <vector>
using namespace std;

int square(int x) {
    return x * x;
}

int main() {
    function<int(int)> f = square;

    cout << f(5) << endl; // 25
}