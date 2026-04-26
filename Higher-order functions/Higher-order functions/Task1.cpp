#include <iostream>
#include <vector>
#include <functional>
using namespace std;
int apply(function<int(int)> func, int x) {
    return func(x);
}