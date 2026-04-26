#include <iostream>
#include <vector>
#include <functional>
using namespace std;
int result =
reduce_custom(
    [](int acc, int x) { return acc + x; },
    map_custom([](int x) { return x * x; }, { 1,2,3,4 }),
    0
);