#include <iostream>
#include <vector>
#include <functional>
using namespace std;
vector<int> process(vector<int> data,
    function<int(int)> transform,
    function<bool(int)> predicate) {
    vector<int> res;

    function<void(int)> rec = [&](int i) {
        if (i == data.size()) return;

        int val = transform(data[i]);
        if (predicate(val))
            res.push_back(val);

        rec(i + 1);
        };

    rec(0);
    return res;
}