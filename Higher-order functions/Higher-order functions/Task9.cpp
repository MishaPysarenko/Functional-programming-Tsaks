#include <iostream>
#include <vector>
#include <functional>
using namespace std;
function<int(int)> multiplier(int n) {
    return [n](int x) {
        return x * n;
        };
}