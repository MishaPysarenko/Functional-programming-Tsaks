#include <iostream>
#include <vector>
#include <functional>
using namespace std;
vector<int> filter_custom(function<bool(int)> func, vector<int> data) {
    vector<int> res;

    function<void(int)> rec = [&](int i) {
        if (i == data.size()) return;
        if (func(data[i])) res.push_back(data[i]);
        rec(i + 1);
        };

    rec(0);
    return res;
}