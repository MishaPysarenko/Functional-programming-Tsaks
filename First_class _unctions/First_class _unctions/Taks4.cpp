#include <iostream>
#include <functional>
#include <vector>
using namespace std;

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }
int sub(int a, int b) { return a - b; }

int calculate(function<int(int, int)> op, int a, int b) {
    return op(a, b);
}