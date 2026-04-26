#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>
#include <ctime>
using namespace std;

map<int, int> cache;

int slow_function(int x) {
    if (cache.count(x)) return cache[x];

    int result = x * x; // heavy computation simulation
    cache[x] = result;
    return result;
}