#include <iostream>
#include <vector>
#include <functional>
using namespace std;
int reduce_custom(function<int(int, int)> func,
    vector<int> data,
    int initial) {
    function<int(int, int)> rec = [&](int i, int acc) {
        if (i == data.size()) return acc;
        return rec(i + 1, func(acc, data[i]));
        };

    return rec(0, initial);
}