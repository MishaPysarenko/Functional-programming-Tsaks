#include <iostream>
#include <vector>
#include <functional>
using namespace std;
int apply(function<int(int)> func, int x) {
    return func(x);
}

void main() {
    auto add = [](int a, int b) { return a + b; };
    auto mul = [](int a, int b) { return a * b; };
    auto pow = [](int a, int b) {
        int r = 1;
        for (int i = 0; i < b; i++) r *= a;
        return r;
        };
}