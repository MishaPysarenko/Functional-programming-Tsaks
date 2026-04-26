#include <iostream>
#include <functional>
#include <vector>
using namespace std;

vector<int> map_custom(function<int(int)> func, vector<int> data) {
    vector<int> res;

    function<void(int)> rec = [&](int i) {
        if (i == data.size()) return;
        res.push_back(func(data[i]));
        rec(i + 1);
        };

    rec(0);
    return res;
}