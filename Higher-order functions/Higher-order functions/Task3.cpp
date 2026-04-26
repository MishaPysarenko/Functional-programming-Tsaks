#include <iostream>
#include <vector>
#include <functional>
using namespace std;
vector<int> transform(vector<int> data, function<int(int)> func) {
    vector<int> res;
    function<void(int)> rec = [&](int i) {
        if (i == data.size()) return;
        res.push_back(func(data[i]));
        rec(i + 1);
        };
    rec(0);
    return res;
}