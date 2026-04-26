#include <iostream>
#include <functional>
#include <vector>
using namespace std;

int apply(function<int(int)> func, int x) {
    return func(x);
}