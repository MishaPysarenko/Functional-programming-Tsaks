#include <iostream>
#include <functional>
#include <vector>
using namespace std;

function<int(int)> multiplier(int n) {
    return [n](int x) {
        return x * n;
        };
}