#include <iostream>
#include <vector>
#include <functional>
using namespace std;
function<bool(int)> make_filter(int n) {
    return [n](int x) {
        return x > n;
        };
}