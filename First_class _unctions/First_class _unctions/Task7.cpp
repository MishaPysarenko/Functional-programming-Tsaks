#include <iostream>
#include <functional>
#include <vector>
using namespace std;

function<int(int)> make_adder(int n) {
    return [n](int x) {
        return x + n;
        };
}